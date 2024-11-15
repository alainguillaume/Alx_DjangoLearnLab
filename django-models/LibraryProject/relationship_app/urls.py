from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('books/', list_books, name='list_books'), 
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'), 
   
]