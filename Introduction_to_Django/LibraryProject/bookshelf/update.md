from bookshelf.models import 
Book book = Book.objects.get(title='New book') 
book.title="Nineteen Eighty-Four" 
book.save()