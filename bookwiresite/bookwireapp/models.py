from django.db import models

class Book(models.Model):
    title = models.TextField()
    author = models.TextField(blank=True)
    description = models.TextField(blank=True)
    ownerUsername = models.TextField()
    borrowerUsername = models.TextField(blank=True)
    datepublished = models.DateField(blank=True)
    isbnthirteen = models.TextField()
    publisher = models.TextField()
    datelastmodified = models.DateTimeField(auto_now=True)