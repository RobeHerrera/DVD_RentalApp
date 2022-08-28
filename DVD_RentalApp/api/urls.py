from django.urls import path
from . import views
  
urlpatterns = [
    path('movies/', views.ListCreateMovieAPIView.as_view(), name='get_post_movies'),
    path('movies/<int:pk>/', views.RetrieveUpdateDestroyMovieAPIView.as_view(), name='get_delete_update_movie'),
]