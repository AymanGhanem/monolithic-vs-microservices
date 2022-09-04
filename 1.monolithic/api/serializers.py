from rest_framework import serializers
from .models import Movie, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class MovieReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'reviewer', 'content']

class MovieSerializer(serializers.ModelSerializer):
    reviews = MovieReviewsSerializer(many=True, required= False)
    class Meta:
        model = Movie 
        fields = ['id', 'title', 'description', 'reviews', ]

    def create(self, validated_data):
        reviews = validated_data.pop('reviews') if validated_data.get('reviews') else []
        movie = Movie.objects.create(**validated_data)
        for review in reviews:
            Review.objects.create(movie=movie, **review)
        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance