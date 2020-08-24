from rest_framework import serializers
from .models import Movies, WatchList
from django.contrib.auth.models import User


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'


class WatchListSerializer(serializers.ModelSerializer):
    movie_id = serializers.SlugRelatedField(queryset=Movies.objects.all(), slug_field='id')
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = WatchList
        fields = ['created_at', 'movie_id', 'user_id', 'watched']

