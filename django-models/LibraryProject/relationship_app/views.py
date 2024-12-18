from typing import Any
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden
from .models import UserProfile
from django.contrib.auth.decorators import permission_required



@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    # Implementation for adding a book
    pass

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    # Implementation for editing a book
    pass

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    # Implementation for deleting a book
    pass



@permission_required('relationship_app.can_change_book', raise_exception=True)
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

    template_name = 'relationship_app/login.html'

class LogoutView(logout):
    template_name = 'relationship_app/logout.html'


# Test function for checking if the user is an Admin
def is_admin(user):
    return user.userprofile.role == 'Admin'

# Test function for checking if the user is a Librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Test function for checking if the user is a Member
def is_member(user):
    return user.userprofile.role == 'Member'

# Admin view: only accessible by Admin users
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view: only accessible by Librarian users
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view: only accessible by Member users
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')