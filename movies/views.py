from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Avg
from .serializers import MovieModelSerializer, MovieStatsSerializer
from app.permissions import GlobalDefaultPermission

from .models import Movie
from reviews.models import Review


class MovieCreateListView (generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer


class MovieRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer


class MovieStatsView(views.APIView):

    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('gender__name').annotate(total=Count('id'))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        movie_stats = {
            'total_movies': total_movies,
            'movies_by_genre': movies_by_genre,
            'total_reviews': total_reviews,
            'average_stars': round(average_stars, 1) if average_stars else 0,
        }

        serializer = MovieStatsSerializer(data=movie_stats)
        serializer.is_valid(raise_exception=True)

        return response.Response(data=serializer.validated_data, status=status.HTTP_200_OK)
