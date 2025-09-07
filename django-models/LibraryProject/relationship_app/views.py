from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.http import HttpResponse
from .models import Library, Book, UserProfile
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

class SignUpView(CreateView):
    form_class = UserCreationForm()
    template_name = 'templates/relationship_app/register.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

def is_admin(user):
    return user.is_authenticated and user.groups.filter(name="Admin").exists()

@user_passes_test(is_admin)
def Admin(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(lambda u: u.is_Librarian)
def Librarian(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(lambda u: u.is_Member)
def Member(request):
    return render(request, 'relationship_app/member_view.html')

@permission_required("relationship_app.can_add_book")
def add_book(request):
    return render(request, 'relationship_app/add_book_view.html')

@permission_required("relationship_app.can_change_book")
def change_book(request):
    return render(request, 'relationship_app/change_book_view.html')

@permission_required("relationship_app.can_delete_book")
def delete_book(request):
    return render(request, 'relationship_app/delete_book_view.html')
# Create your views here.
