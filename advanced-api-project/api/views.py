from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Book
from .serializers import BookSerializer

class ListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ListAPIView(ReadOnlyModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DetailView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CreateView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UpdateView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DeleteView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
# Create your views here.
