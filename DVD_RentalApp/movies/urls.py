from django.urls import path
from . import views

"""
End points for Movies Django app
"""
urlpatterns = [
    path('list/', views.index, name="movies_index"),
    path('list/<int:movie_id>', views.detail, name="movies_detail")
]