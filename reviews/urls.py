from django.urls import path
from .views import ReviewCreateListView, ReviewRetriveUpdateDestryView

urlpatterns = [
    path('reviews', ReviewCreateListView.as_view(), name='review-create-list'),
    path('reviews/<int:pk>', ReviewRetriveUpdateDestryView.as_view(), name='review-detail-view'),
]
