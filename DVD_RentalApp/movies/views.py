from django.shortcuts import render, get_object_or_404
from . models import Movie

from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Movie
from .serializers import MovieSerializer
from .pagination import CustomPagination
from .filters import MovieFilter
from datetime import datetime


def index(request):
    """
    View to render the list of all the movies.

    Args:
      request: requst from http url.

    Returns:s
      render of  movies/index.
    """
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):
    """
    View to render the dedtails for each element of the movie list.

    Args:
    request: requst from http url.
    pk: primary key for the movie

    Returns:
    render of  movies/detail.
    """
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})


class ListCreateMovieAPIView(ListCreateAPIView):
    """
    Class heritage ListCreateAPIView that create the methods GET | POST for us. 
    """
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MovieFilter

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
        serializer.save(date_created=dt_string)


class RetrieveUpdateDestroyMovieAPIView(RetrieveUpdateDestroyAPIView):
    """
    Class heritage RetrieveUpdateDestroyAPIView that create the methods UPDATE | DLEETE for us. 
    """
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated]