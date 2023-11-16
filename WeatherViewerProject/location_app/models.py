from django.db import models


# Create your models here.
from users_app.models import Users


class Locations(models.Model):
    Name = models.CharField(max_length=255, null=False)
    Userid = models.ForeignKey(Users, on_delete=models.CASCADE, null=False)
    Latitude = models.DecimalField(max_digits=18, decimal_places=5)
    Longitude = models.DecimalField(max_digits=18, decimal_places=5)
