from django.urls import path
from .views import list_books, LibraryDetailView, admin_view
from .views import SignUpView
from .views import LoginView
from .views import LogoutView
from .views import admin_view
from .views import librarian_view
from .views import member_view


urlpatterns = [
    path('books/', list_books, name='list_books'), 
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'), 
    path('views.register/', SignUpView.as_view(), name='register'),
    path('login/',  LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    # path('profile/', admin_view, name='profile'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),

]