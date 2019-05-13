from django.db import models
from django.urls import reverse

class Booklist(models.Model):

    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    pages = models.IntegerField(default=0)
    author = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('booklist')

