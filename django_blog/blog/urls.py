from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from blog.views import SignUpView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),
    path('profile/', )

]