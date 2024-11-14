from django.db import models

# Create your models here.
#Author: name CharField
#Book:  title CharField, author ForeignKey to Author
#Library:  name CharField, books ManyToManyField to Book
#Librarian: name CharField, library OneToOneField to Library

class Author(models.Model):
    name = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='authors')

class Library(models.Model):
    name = models.CharField(max=30)
    books = models.ManyToManyField(Book, related_name='libralies')

class Librarian(models.Model):
    name = models.CharField(max_length=30)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
