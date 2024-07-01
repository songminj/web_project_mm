from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    finance_goal = models.CharField(max_length=100, default='금일 저녁식사 해결')
    nickname = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    assets = models.FloatField(default=0)
    salary = models.FloatField(default=0)