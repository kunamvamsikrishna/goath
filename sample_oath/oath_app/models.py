from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    role = models.CharField(null=True,blank=True)
    age = models.IntegerField(null = True,blank=True)