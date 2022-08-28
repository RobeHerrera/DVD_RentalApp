from django.shortcuts import render
from movies.models import Movie
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .pagination import CustomPagination
from .filters import FilmFilter
from .serializers import FilmSerializer
from datetime import datetime
from movies.models import (
    Genre, Movie, Actor, Address, Category, City, Country, Customer,
    FilmCategory, Film, Inventory, Language, Payment, Rental, Staff, Store
    )


# def getMovie(request, pk):
#     """
#     View to render the details of the movies.

#     Args:
#       request: requst from http url.

#     Returns:
#       render of  movies/details.
#     """
#     movie = Movie.objects.get(id = pk)
#     return render(request, 'movies/detail.html', {'movie': movie})

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
        View to render the dedtails for each element of the movie list.

        Args:
        request: requst from http url.
        pk: primary key for the movie

        Returns:
        render of  movies/detail.
        """
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d")
        serializer.save(last_update=dt_string)


class RetrieveUpdateDestroyMovieAPIView(RetrieveUpdateDestroyAPIView):
    """
    Class heritage RetrieveUpdateDestroyAPIView that create the methods UPDATE | DLEETE for us. 
    """
    serializer_class = FilmSerializer
    queryset = Film.objects.all()
    permission_classes = [IsAuthenticated]