from .models import Book, Author, Librarian, Library
# Query all books by a specific author.
# List all books in a library.
# Retrieve the librarian for a library.
books = Book.objects.filter(Author.name)
books = Book.objects.all(Library.objects.get(name="library_name"),books.all())

