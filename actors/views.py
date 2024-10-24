from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import ActorSerializer

from app.permissions import GlobalDefaultPermission

from .models import Actor

#Lista Todos ou Adiciona Atores
class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

#Lista, Altera ou Exclui um Ator Específico
class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
