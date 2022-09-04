from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Movie
from .serializers import  MovieSerializer
import requests

def extend_movie(movie):
            # Hard Coded URL for reviews microservice
            url = "http://localhost:8001/api/reviews/"
            response = requests.get(url).json()
            reviews = []
            for review in response:
                if(review.get('movie', -1) == movie.id):
                    review_object = {
                        "id": review.get('id', None),
                        "content": review.get('content', None),
                        "reviewer": review.get('reviewer', None)
                    }
                    reviews.append(review_object)
            return {
                "id": movie.id,
                "title": movie.title,
                "description": movie.description,
                "reviews": reviews
            }


# When the movie is deleted, all its reviews must be deleted also. # Change#3
def delete_reviews(movie_id):
            # Hard Coded URL for reviews microservice
            url = "http://localhost:8001/api/reviews/"
            response = requests.get(url).json()
            reviews = []
            for review in response:
                if(review.get('movie', -1) == movie_id):
                    reviews.append(review.get("id"))
            for review_id in reviews:
                requests.delete(url + f"{review_id}/")

class MovieList(APIView):
    """
    List all snippets, or create a new movie.
    """
    def get(self, request, format=None):
        movies_qs = Movie.objects.all()
        # serializer = MovieSerializer(movies_qs, many=True)
        return Response([extend_movie(movie) for movie in movies_qs], status= status.HTTP_200_OK) # Change #1
    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieDetail(APIView):
    """
    Retrieve, update or delete a movie instance.
    """
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Exception()

    def get(self, request, pk, format=None):
        try:
            movie = self.get_object(pk)
        except:
            return Response(status= status.HTTP_404_NOT_FOUND)
        # serializer = MovieSerializer(movie)
        return Response([extend_movie(movie)], status= status.HTTP_200_OK) # Change #2

    def put(self, request, pk, format=None):
        try:
            movie = self.get_object(pk)
        except:
            return Response(status= status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            movie = self.get_object(pk)
            delete_reviews(movie.id)
        except:
            return Response(status= status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)