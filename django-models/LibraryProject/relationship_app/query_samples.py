# to query books by specific author:
from relationship_app.models import Book, Librarian, Library
for books in Book.objects.all():
    if books.author == "author":
        print(books.title)

Library.objects.get(name="library_name"), books.all()

Librarian.objects.get(library="library_name")
