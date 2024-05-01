from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    author = models.CharField(max_length=200)
