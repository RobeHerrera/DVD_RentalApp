from django_filters import rest_framework as filters
from movies.models import (
    Genre, Movie, Actor, Address, Category, City, Country, Customer,
    FilmCategory, Film, Inventory, Language, Payment, Rental, Staff, Store
    )


class MovieFilter(filters.FilterSet):
    """
    We create filters for each field we want to be able to filter on
    """
    title = filters.CharFilter(lookup_expr='icontains')
    genre = filters.CharFilter(lookup_expr='icontains')
    year = filters.NumberFilter()
    year__gt = filters.NumberFilter(field_name='year', lookup_expr='gt')
    year__lt = filters.NumberFilter(field_name='year', lookup_expr='lt')

    class Meta:
        model = Movie
        fields = ['title', 'genre', 'year', 'year__gt', 'year__lt']

class FilmFilter(filters.FilterSet):
    """
    We create filters for each field we want to be able to filter on
    """

    class Meta:
        model = Film
        fields = ['id', 'title', 'description', 'release_year', 'language','rental_duration',
        'rental_rate','length','replacement_cost','rating','last_update','special_features','fulltext']

