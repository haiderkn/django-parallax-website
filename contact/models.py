from django.db import models

# Create your models here.
class ContactModel(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=25)
    ask = models.CharField(max_length=255)