from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Videos(models.Model):
    course_name = models.CharField(max_length=256)
    course_id = models.IntegerField()
    video_link = models.URLField()
    video_title = models.CharField(max_length=2048)
    inserted_datetime = models.DateTimeField(auto_now_add=True)