from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=100, unique= True)
    