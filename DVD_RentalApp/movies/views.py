from django.shortcuts import render, get_object_or_404
from .models import (
    Genre, Movie, Actor, Address, Category, City, Country, Customer,
    FilmCategory, Film, Inventory, Language, Payment, Rental, Staff, Store
    )


def index(request):
    """
    View to render the list of all the movies.

    Args:
      request: requst from http url.

    Returns:s
      render of  movies/index.
    """
    movies = Film.objects.all()
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
    movie = get_object_or_404(Film, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
    