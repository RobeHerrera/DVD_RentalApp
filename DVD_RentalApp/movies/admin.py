from django.contrib import admin
from .models import Genre, Movie


"""
To show in admin page

TODO: 
    - Add all the tables in the DB of DVD Rental
"""
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created', )
    list_display = ('id', 'title', 'number_in_stocks', 'daily_rate', 'genre')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
