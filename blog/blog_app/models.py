from django.db import models
from datetime import datetime


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    author = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
