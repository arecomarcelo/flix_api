from rest_framework import generics
from .models import Movie
from .serializers import MovieModelSerializer

class MovieCreateListView (generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer

class MovieRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer
