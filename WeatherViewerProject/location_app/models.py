from django.db import models


# Create your models here.
from django.contrib.auth.models import User


class Locations(models.Model):
    Name = models.CharField(max_length=255, null=False)
    Userid = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    Latitude = models.DecimalField(max_digits=18, decimal_places=5)
    Longitude = models.DecimalField(max_digits=18, decimal_places=5)
