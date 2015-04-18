from django.db import models

# Create your models here.


class Devices(models.Model):
    device_1 = models.BooleanField()
    device_2 = models.BooleanField()
    device_3 = models.BooleanField()
    device_4 = models.BooleanField()