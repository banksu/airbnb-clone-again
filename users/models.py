from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):

    """Custum User Model"""
    avatar = models.ImageField()
    gender = models.CharField(max_length=10, null=True)
    bio = models.TextField(default="")
