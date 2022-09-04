from django.contrib import admin
from django.urls import path
from .views import ReviewDetail, ReviewList

urlpatterns = [
    path('reviews/', ReviewList.as_view()),
    path('reviews/<int:pk>/', ReviewDetail.as_view()),
]
