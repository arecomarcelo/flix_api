from django.urls import path
from .views import GenreCreateListView, GenreRetriveCreateListView

urlpatterns = [
    path('genres', GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>', GenreRetriveCreateListView.as_view(), name='genre-detail-view'),
]
