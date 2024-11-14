from django.shortcuts import render
from .models import Book, Library
# Create your views here.

# Implement Function-based View:

# Create a function-based view in relationship_app/views.py that lists all books stored in the database.
# This view should render a simple text list of book titles and their authors.

def book_list(request):
    books = Book.objects.all()
    context = {'book_list': book_list}
    return render(request, 'books/book_list.html', context)