from rest_framework import serializers
from .models import Movie
from django.contrib.auth.models import User


class MovieSerializer(serializers.ModelSerializer):  # create class to serializer model
    class Meta:
        model = Movie

        fields = ('id', 'title', 'release_year', 'number_in_stocks', 'daily_rate','genre')
