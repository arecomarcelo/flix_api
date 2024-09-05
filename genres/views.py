from rest_framework import generics
from genres.models import Genre
from .serializers import GenreSerializer

#Lista Todos ou Adiciona Generos
class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

#Lista, Altera ou Exclui um Genero Específico
class GenreRetriveCreateListView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer