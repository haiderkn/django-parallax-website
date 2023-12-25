from django.db import models

# Create your models here.
class BlogModel(models.Model):
    date = models.DateTimeField()
    writer = models.CharField(max_length=25)
    title = models.CharField(max_length=120)
    blog = models.CharField(max_length=255)
