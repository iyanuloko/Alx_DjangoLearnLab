from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import SignUpView, ProfileView, FollowersView
urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/',FollowersView.as_view(), name='follow' ),
    path('unfollow/<int:user_id/>',FollowersView.as_view(), name='unfollow' ),
]
