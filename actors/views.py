from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import ActorSerializer

from .models import Actor

#Lista Todos ou Adiciona Atores
class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

#Lista, Altera ou Exclui um Ator Específico
class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
