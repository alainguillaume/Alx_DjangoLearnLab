python from bookshelf.models import Book

new_book = Book(title='New book', author='John Doe', publication_year=2020)
new_book.save()