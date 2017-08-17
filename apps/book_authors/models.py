from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return self.__unicode__()


class Author(models.Model):
    first_name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255, blank=True)
    email = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    books = models.ManyToManyField(Book, related_name='authors')
    notes = models.TextField(blank=True)

    def __unicode__(self):
        return "Author: {} {}.".format(self.first_name, self.last_name)

    def __str__(self):
        return self.__unicode__()
