from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from app.permissions import GlobalDefaultPermission

from .serializers import GenreSerializer
from .models import Genre
# from .permissions import GenrePermissionClass ---> Inativado para utilizar a GlobalDefaultPermission


# Lista Todos ou Adiciona Generos
class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


# Lista, Altera ou Exclui um Genero Específico
class GenreRetriveCreateListView (generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
