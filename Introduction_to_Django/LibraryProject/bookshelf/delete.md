from bookshelf.models import Book

book = Book.objects.get(title='New book')
book.delete()