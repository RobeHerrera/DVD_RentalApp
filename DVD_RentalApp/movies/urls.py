from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.index, name="movies_index"),
    path('list/<int:movie_id>', views.detail, name="movies_detail"),
    path('', views.ListCreateMovieAPIView.as_view(), name='get_post_movies'),
    path('<int:pk>/', views.RetrieveUpdateDestroyMovieAPIView.as_view(), name='get_delete_update_movie'),
]