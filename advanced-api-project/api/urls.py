from django.urls import path, include
from .views import ListAPIView, CreateAPIView, DeleteAPIView, DetailAPIView, UpdateAPIView

urlpatterns = [
    path('books/', ListAPIView.as_view(), name='book-list'),
    path('books/<int:pk>/', DetailAPIView.as_view(), name='book-detail'),
    path('books/create/', CreateAPIView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', UpdateAPIView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', DeleteAPIView.as_view(), name='book-delete'),5
]