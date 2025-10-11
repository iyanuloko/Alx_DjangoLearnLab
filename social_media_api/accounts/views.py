from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.authtoken.models import Token
from rest_framework import generics, permissions

from .models import CustomUser
from .serializers import SignUpFormSerializer, ProfileViewSerializer, FollowersSerializer

class ProfileView(LoginRequiredMixin, generics.CreateAPIView):
    serializer_class = ProfileViewSerializer

class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpFormSerializer

class FollowersView(generics.GenericAPIView):
    serializer_class = FollowersSerializer
    permission_classes = (permissions.IsAuthenticated)
    queryset = CustomUser.objects.all()
    def update(self, request, *args, **kwargs):
        if "following" in request.data:
            request.user.following.add(request.data["following"])
            request.user.save()
        if "unfollowing" in request.data:
            request.user.unfollowing.add(request.data["unfollowing"])
            request.user.save()
# Create your views here.
