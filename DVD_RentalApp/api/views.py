from django.shortcuts import render
from movies.models import Movie


def getMovie(request, pk):
    """
    View to render the details of the movies.

    Args:
      request: requst from http url.

    Returns:
      render of  movies/details.
    """
    movie = Movie.objects.get(id = pk)
    return render(request, 'movies/detail.html', {'movie': movie})
