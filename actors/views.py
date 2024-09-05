from rest_framework import generics
from .models import Actor
from .serializers import ActorSerializer

#Lista Todos ou Adiciona Atores
class ActorCreateListView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

#Lista, Altera ou Exclui um Ator Específico
class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
