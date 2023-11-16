from django.db import models


# Create your models here.
class Users(models.Model):
    Login = models.CharField(max_length=255, null=False)
    Password = models.CharField(max_length=255, null=False)
