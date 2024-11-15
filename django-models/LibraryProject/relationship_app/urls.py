from django.urls import path
from .views import list_books, LibraryDetailView

urlpartens = [
    path('book/', list_books, name='book'),
    path('libary/', LibraryDetailView.as_view(), name='libraly'),

]