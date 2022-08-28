from django.apps import AppConfig


class MoviesConfig(AppConfig):
    """
    Configuration for the movie app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movies'
