from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=255)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    birth_place = models.CharField(null=True, blank=True)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)

class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name="groups")