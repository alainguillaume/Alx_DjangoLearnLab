from django.contrib.auth.models import User
from django.db import models

# Create your models here.
#Author: name CharField
#Book:  title CharField, author ForeignKey to Author
#Library:  name CharField, books ManyToManyField to Book
#Librarian: name CharField, library OneToOneField to Library

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='authors')


    class Meta:
        permissions = (
            ('can_add_book', 'Can add a new book'),
            ('can_change_book', 'Can edit an existing book'),
            ('can_delete_book', 'Can delete a book'),
        )

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max=30)
    books = models.ManyToManyField(Book, related_name='libralies')

    

class Librarian(models.Model):
    name = models.CharField(max_length=30)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

class UserProfile(models.Model):
    ADMIN = 'admin'
    LIBRARIAN = 'librarian'
    MEMBER = 'member'
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (LIBRARIAN, 'Librarian'),
        (MEMBER, 'Member'),
    ]
 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"
