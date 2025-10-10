from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.authtoken.models import Token
from rest_framework import generics
from .serializers import SignUpFormSerializer, ProfileViewSerializer

class ProfileView(LoginRequiredMixin, generics.CreateAPIView):
    serializer_class = ProfileViewSerializer

class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpFormSerializer

# Create your views here.
