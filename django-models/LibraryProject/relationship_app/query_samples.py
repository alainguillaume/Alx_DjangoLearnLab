from .models import Book, Author
# Query all books by a specific author.
# List all books in a library.
# Retrieve the librarian for a library.
books = Book.objects.filter(Author.name)
books = Book.objects.all()

