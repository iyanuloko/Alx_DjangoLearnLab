from django.shortcuts import render
from .forms import ExampleForm

@permission_required("bookshelf.can_view")
def view_book(request):
    return render(request, 'relationship_app/book_list.html')

@permission_required("bookshelf.can_edit", raise_exception=True)
def change_book(request):
    return render(request, 'relationship_app/change_book_view.html')

@permission_required("bookshelf.can_create")
def add_book(request):
    return render(request, 'relationship_app/delete_book_view.html')

@permission_required("bookshelf.can_delete")
def delete_book(request):
    return render(request, 'relationship_app/delete_book_view.html')

def contact_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # handle the data — e.g., save to DB, send email, etc.
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # message = form.cleaned_data['message']
            return redirect('bookshelf/form_example')  # change target as needed
    else:
        form = ContactForm()
# Create your views here.
