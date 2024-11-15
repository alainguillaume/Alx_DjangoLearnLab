from django.urls import path
from .views import list_books, LibraryDetailView
from .views import SignUpView
from .views import LogInView
from .views import LogOutView


urlpatterns = [
    path('books/', list_books, name='list_books'), 
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'), 
    path('views.register/', SignUpView.as_view(), name='register'),
    path('login/', LogInView.as_view(template_name = 'relationship_app/login.html')),
    path('logut/', LogOutView.as_view( template_name = 'relationship_app/logout.html')),
]