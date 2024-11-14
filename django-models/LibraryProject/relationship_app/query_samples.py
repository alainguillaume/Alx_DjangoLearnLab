from .models import Book, Author, Librarian, Library
# Query all books by a specific author.
# List all books in a library.
# Retrieve the librarian for a library.
books_by_author= ["Author.objects.get(name=author_name)"]
library = Library.objects.get(name="library_name")
books = ["Library.objects.get(name=library_name)", "books.all()"]
librarian = library.librarian




