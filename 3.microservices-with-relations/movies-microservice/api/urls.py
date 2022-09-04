from django.contrib import admin
from django.urls import path
from .views import MovieList, MovieDetail, MovieList

urlpatterns = [
    path('movies/', MovieList.as_view()),
    path('movies/<int:pk>/', MovieDetail.as_view()),
]