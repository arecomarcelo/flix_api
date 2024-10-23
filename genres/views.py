from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import GenreSerializer
from .models import Genre
from .permissions import GenrePermissionClass

#Lista Todos ou Adiciona Generos
class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GenrePermissionClass,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

#Lista, Altera ou Exclui um Genero Específico
class GenreRetriveCreateListView (generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GenrePermissionClass,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer