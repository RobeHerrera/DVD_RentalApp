from django.shortcuts import render, get_object_or_404
from movies.models import Movie
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters import rest_framework as filters
from .pagination import CustomPagination
from .filters import FilmFilter
from .serializers import FilmSerializer, RentMovieSerializer
from datetime import datetime
from movies.models import (
    Genre, Movie, Actor, Address, Category, City, Country, Customer,
    FilmCategory, Film, Inventory, Language, Payment, Rental, Staff, Store
    )


########################################  Create API for Movies / Films #########################################################
class ListCreateMovieAPIView(ListCreateAPIView):
    """
    Class heritage ListCreateAPIView that create the methods GET | POST for us. 
    """
    serializer_class = FilmSerializer
    queryset = Film.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FilmFilter

    def perform_create(self, serializer):
        """
        View to render the details for each element of the movie list.
        """
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d")
        serializer.save(last_update=dt_string)


class RetrieveUpdateDestroyMovieAPIView(RetrieveUpdateDestroyAPIView):
    """
    Class heritage RetrieveUpdateDestroyAPIView that create the methods UPDATE | DELETE for us. 
    """
    serializer_class = FilmSerializer
    queryset = Film.objects.all()
    permission_classes = [IsAuthenticated]


########################################  Create API for Rent a DVD Movie #########################################################
class RentMovieAPIView(ListCreateAPIView):
    """
    Class heritage ListCreateAPIView that create the methods GET | POST for us. 
    """
    serializer_class = RentMovieSerializer
    queryset = Rental.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    # filterset_class = FilmFilter

    def perform_create(self, serializer):
        """
        View to render the details for each element of the movie list.
        """
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d")
        serializer.save(last_update=dt_string)

class ReturnMovieAPIView(RetrieveUpdateDestroyAPIView):
    """
    Class heritage RetrieveUpdateDestroyAPIView that create the methods UPDATE | DELETE for us. 
    """
    serializer_class = RentMovieSerializer
    queryset = Rental.objects.all()
    permission_classes = [IsAuthenticated]