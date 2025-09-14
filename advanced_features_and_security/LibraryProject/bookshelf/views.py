from django.shortcuts import render
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

# Create your views here.
