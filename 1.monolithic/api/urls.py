from django.contrib import admin
from django.urls import path
from .views import MovieList, MovieDetail, MovieList, ReviewDetail, ReviewList

urlpatterns = [
    path('movies/', MovieList.as_view()),
    path('movies/<int:pk>/', MovieDetail.as_view()),
    path('reviews/', ReviewList.as_view()),
    path('reviews/<int:pk>/', ReviewDetail.as_view()),
]
