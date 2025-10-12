from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics, permissions
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from accounts.models import CustomUser
from notifications.models import Notification
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class UserFeed(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = PostSerializer
    def list(self, request, *args, **kwargs):
        following_users = request.user.following.all()
        feed_posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(feed_posts, many=True)
        return Response(serializer.data)

class Like(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    def create(self, request, *args, **kwargs):
        post = generics.get_object_or_404(Post, pk=pk)
        Like.objects.get_or_create(user=request.user, post=post)
        Notification.objects.create()
        serializer = PostSerializer(post)
        return Response(serializer.data)
# Create your views here.
