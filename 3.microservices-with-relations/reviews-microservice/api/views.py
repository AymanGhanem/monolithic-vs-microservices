from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import requests

from .models import Review
from .serializers import ReviewSerializer

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
        movie = request.data.get("movie")
        # Check whether this movies exist.  # Change #4.
        try:
            url = f"http://localhost:8000/api/movies/{movie}/"
            response = requests.head(url)
            if(response.status_code != 200):
                return Response({"error": f"This implied movie does not exsist!"}, status= status.HTTP_404_NOT_FOUND)
        except:
            return Response({"error": f"Something went wrong!"}, status= status.HTTP_400_BAD_REQUEST)
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
        # Check whether this movies exist.  # Change #5.
        try:
            movie = request.data.get("movie")
            url = f"http://localhost:8000/api/movies/{movie}/"
            response = requests.head(url)
            print(response)
            print(type(response))
            if(response.status_code != 200):
                return Response({"error": f"This implied movie does not exsist!"}, status= status.HTTP_404_NOT_FOUND)
        except:
            return Response({"error": f"Something went wrong!"}, status= status.HTTP_400_BAD_REQUEST)
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
