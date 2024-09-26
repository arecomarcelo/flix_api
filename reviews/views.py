from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import ReviewSerializer

from .models import Review

class ReviewCreateListView (generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewRetriveUpdateDestryView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer        
