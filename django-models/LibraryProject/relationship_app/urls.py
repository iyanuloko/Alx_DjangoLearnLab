from django.contrib import admin
from django.urls import path
from . import views
from .views import list_books, LibraryDetailView
urlpatterns = [
    path('book_list/', views.list_books, name='book_list'),
    path('books_in_library/', views.LibraryDetailView.as_view(), name='books_in_library'),
]