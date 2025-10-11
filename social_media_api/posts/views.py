from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from accounts.models import User
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class UserFeed(generics.ListAPIView):
    following_users = User.objects.filter(is_following=True)
    queryset = User.objects.all()
    serializer_class = PostSerializer
    def list(self, request, *args, **kwargs):
        feed_posts = Post.objects.filter(following_users=self.following_users)
        feed_posts = feed_posts.order_by('-created_at')
        serializer = PostSerializer(feed_posts, many=True, data=request.data)
        return Response(serializer.data)
# Create your views here.
