from django.urls import path
from .views import MovieCreateListView, MovieRetriveUpdateDestroyView


urlpatterns = [
    path('movies', MovieCreateListView.as_view(), name='movie-create-list'),
    path('movies/<int:pk>', MovieRetriveUpdateDestroyView.as_view(),name='movie-detail-view'),
]