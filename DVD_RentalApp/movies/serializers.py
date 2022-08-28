from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):  # create class to serializer model
    """
    Serializer for rest framework
    """
    class Meta:
        model = Movie

        fields = ('id', 'title', 'release_year', 'number_in_stocks', 'daily_rate','genre')
