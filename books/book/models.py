from django.db import models
from django.urls import reverse

class Choice(models.Model):

    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('booklist')