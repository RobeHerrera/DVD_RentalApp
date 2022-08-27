from django.shortcuts import render
from movies.models import Movie


def getMovie(request, pk):
    movie = Movie.objects.get(id = pk)
    return render(request, 'movies/detail.html', {'movie': movie})
