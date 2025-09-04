# to query books by specific author:
from relationship_app.models import Book, Librarian
for book in Book.objects.all():
    if book.author == "author":
        print(book.title)

for book in Book.objects.all():
    print(book)

for librarian in Librarian.objects.all():
    if librarian.library == "library":
        print(librarian.name)