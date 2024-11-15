from typing import Any
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import UserProfile
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import admin



def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = Library
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['book_list'] = library.get_book_list()

class SignUpView(CreateView):
    from_class = UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

class LoginView(login):
    template_name = 'relationship_app/login.html'

class LogoutView(logout):
    template_name = 'relationship_app/logout.html'

@admin
def Admin(request):
    UserProfile = UserProfile.objects.all()
    return render(request, 'relationship_app/profile.html', {'userProfile': UserProfile})







