from django.shortcuts import render
from movies.models import Movie

# from rest_framework.response import Response
# from rest_framework.decorators import api_view

# # Create your views here.
# @api_view(['GET'])
# def getData(request):
#     person = 

def getMovie(request, pk):
    movie = Movie.objects.get(id = pk)
    return render(request, 'movies/detail.html', {'movie': movie})
