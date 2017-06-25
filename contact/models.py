from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=512)
    subject = models.TextField(max_length=1024)
    message = models.TextField(max_length=8192)
    inserted_datetime = models.DateTimeField(auto_now_add=True)