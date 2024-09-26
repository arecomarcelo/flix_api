from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import GenreSerializer

from genres.models import Genre

#Lista Todos ou Adiciona Generos
class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

#Lista, Altera ou Exclui um Genero Específico
class GenreRetriveCreateListView (generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer