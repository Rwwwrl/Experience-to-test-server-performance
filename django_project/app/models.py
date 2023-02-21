from django.db import models


class Author(models.Model):

    name = models.CharField(max_length=100)


class Book(models.Model):

    author = models.ForeignKey(Author, related_name='books', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
