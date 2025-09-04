from django.shortcuts import render
from django.http import HttpResponse
from .models import Library, Book
from django.views.generic.detail import DetailView
def book_list(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

class books_in_library(DetailView):
    model = Library
    template_name = 'library_detail.html'

# Create your views here.
