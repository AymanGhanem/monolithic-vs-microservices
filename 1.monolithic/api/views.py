from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Movie, Review
from .serializers import  MovieSerializer, ReviewSerializer

class MovieList(APIView):
    """
    List all snippets, or create a new movie.
    """
    def get(self, request, format=None):
        movies_qs = Movie.objects.all()
        serializer = MovieSerializer(movies_qs, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

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
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status= status.HTTP_200_OK)

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
        except:
            return Response(status= status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReviewList(APIView):
    """
    List all snippets, or create a new review.
    """
    def get(self, request, format=None):
        reviews_qs = Review.objects.all()
        serializer = ReviewSerializer(reviews_qs, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewDetail(APIView):
    """
    Retrieve, update or delete a review instance.
    """
    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise Exception()

    def get(self, request, pk, format=None):
        try:
            review = self.get_object(pk)
        except:
            return Response(status= status.HTTP_404_NOT_FOUND)
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status= status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        try:
            review = self.get_object(pk)
        except:
            return Response(status= status.HTTP_404_NOT_FOUND)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            review = self.get_object(pk)
        except:
            return Response(status= status.HTTP_404_NOT_FOUND)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

