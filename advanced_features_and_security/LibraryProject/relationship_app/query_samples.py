# to query books by specific author:
from relationship_app.models import Author, Book, Librarian, Library
for books in Book.objects.all():
    if books.author == "author":
        print(books.title)

library_books = Library.objects.get(name=library_name)
print(library_books.books.all())

author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)

librarians = Librarian.objects.get(library=library_name)
print(librarians.name)