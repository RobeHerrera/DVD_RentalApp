from rest_framework import viewsets
from movies import models
from . import serializers

class MovieViewset(viewsets.ModelViewSet):
    queryset = models.Movie.objects.all()
    serializers_class = serializers.MovieSerializer