from django.urls import path
from .views import list_books, LibraryDetailView, admin_view
from .views import SignUpView
from .views import LoginView
from .views import LogoutView
from .views import admin_view
from .views import librarian_view
from .views import member_view
from .views import add_book
from .views import edit_book
from .views import delete_book


urlpatterns = [
    path('books/', list_books, name='list_books'), 
     path('add_book/', add_book, name='add_book'),  # Add URL for adding a book
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),  # URL for editing a book
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),  # URL for deleting a book
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'), 
    path('views.register/', SignUpView.as_view(), name='register'),
    path('login/',  LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    # path('profile/', admin_view, name='profile'),
    path('Admin/', admin_view, name='admin_view'),
    path('Librarian/', librarian_view, name='librarian_view'),
    path('Member/', member_view, name='member_view'),

]