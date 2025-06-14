from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(unique=True, max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
