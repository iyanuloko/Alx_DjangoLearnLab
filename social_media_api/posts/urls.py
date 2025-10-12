from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, UserFeed, Like

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('posts/', include(router.urls)),
    path('/feed/', UserFeed().as_view(), name='feed'),
    path('posts/<int:pk>/like/', Like.as_view(), name='like'),
    path('posts/<int:pk>/unlike/', Like.as_view(), name='unlike'),
]