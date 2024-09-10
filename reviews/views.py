from rest_framework import generics
from .serializers import ReviewSerializer

from .models import Review

class ReviewCreateListView (generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewRetriveUpdateDestryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer        
