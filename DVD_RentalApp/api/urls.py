from django.urls import path
from . import views
  
urlpatterns = [
    path('movies/', views.ListCreateMovieAPIView.as_view(), name='get_post_movies'),
    path('movies/<int:pk>/', views.RetrieveUpdateDestroyMovieAPIView.as_view(), name='get_delete_update_movie'),

    path('rental/', views.RentMovieAPIView.as_view(), name='list_rental'),
    path('rental/<int:pk>/', views.ReturnMovieAPIView.as_view(), name='single_rental'),

    # path('payment/', views.RetrieveUpdateDestroyMovieAPIView.as_view(), name='get_delete_update_movie'),
    # path('payment/<int:pk>/', views.RetrieveUpdateDestroyMovieAPIView.as_view(), name='get_delete_update_movie'),
    # path('inventory/', views.RetrieveUpdateDestroyMovieAPIView.as_view(), name='get_delete_update_movie'),
    # path('inventory/<int:pk>/', views.RetrieveUpdateDestroyMovieAPIView.as_view(), name='get_delete_update_movie'),
    # path('Staff/', views.RetrieveUpdateDestroyMovieAPIView.as_view(), name='get_delete_update_movie'),
    # path('Staff/<int:pk>/', views.RetrieveUpdateDestroyMovieAPIView.as_view(), name='get_delete_update_movie'),
]