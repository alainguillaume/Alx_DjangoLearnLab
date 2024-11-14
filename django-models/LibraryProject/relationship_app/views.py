from django.shortcuts import render
from django.views.generic import DeleteView
from .models import Book
from .models import Library
# Create your views here.

# Implement Function-based View:

# Create a function-based view in relationship_app/views.py that lists all books stored in the database.
# This view should render a simple text list of book titles and their authors.

def book_list(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'relationship_app/list_books.html', context)

def libraly_list(request):
    libralies = Library.objects.all()
    context = {'libraly_list': libralies}
    return render(request, 'relationship_app/library_detail.html', context)