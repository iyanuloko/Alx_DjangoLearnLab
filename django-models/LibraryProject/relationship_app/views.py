from django.contrib.auth.decorators import user_passes_test, login_required
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
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"

def is_librarian(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Librarian"

def is_member(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Member"

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member)
def member_view(request):
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
