from rest_framework import serializers
from movies.models import (
    Genre, Movie, Actor, Address, Category, City, Country, Customer,
    FilmCategory, Film, Inventory, Language, Payment, Rental, Staff, Store
    )


class FilmSerializer(serializers.ModelSerializer):  # create class to serializer model
    """
    Serializer for rest framework
    """
    class Meta:
        model = Film

        fields = ('id', 'title', 'description', 'release_year', 'language','rental_duration',
        'rental_rate','length','replacement_cost','rating','last_update','special_features','fulltext')

class MovieSerializer(serializers.ModelSerializer):  # create class to serializer model
    """
    Serializer for rest framework
    """
    class Meta:
        model = Movie
        fields = ('id', 'title', 'release_year', 'number_in_stocks', 'daily_rate','genre')

class RentMovieSerializer(serializers.ModelSerializer): 
    rental_date = serializers.CharField(max_length=1000, required=True)

    class Meta:
        model = Rental
        fields = ('id', 'rental_date', 'inventory' , 'customer', 'return_date', 'staff', 'last_update')
