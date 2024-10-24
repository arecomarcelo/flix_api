from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import MovieModelSerializer
from app.permissions import GlobalDefaultPermission
from .models import Movie

class MovieCreateListView (generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer

class MovieRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer
