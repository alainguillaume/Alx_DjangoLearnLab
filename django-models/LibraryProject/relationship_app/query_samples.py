from .models import Book, Author, Librarian, Library
# Query all books by a specific author.
# List all books in a library.
# Retrieve the librarian for a library.
author = Author.objects.get(name="author_name")
books_by_author= Book.objects.filter(author=author)

library = Library.objects.get(name="library_name")
books = ["Library.objects.get(name=library_name)", "books.all()"]
librarian = library.librarian




