from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView, SignUpView
urlpatterns = [
    path('book_list/', views.list_books, name='book_list'),
    path('books_in_library/', views.LibraryDetailView.as_view(), name='books_in_library'),
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='templates/relationship_app/login.html'), name='login'),\
    path('logout/', LogoutView.as_view(template_name='templates/relationship_app/logout.html'), name='logout'),
    path('signup/', views.register, name='signup'),
    path('admin/', views.admin_view, name='admin'),
    path('librarian', views.librarian_view, name='librarian'),
    path('member', views.member_view, name='member'),
]