from django.db import models

# Create your models here.
class AllowedGpio(models.Model):
    gpios = models.CharField()