from django.db import models

# Create your models here.
class Appliance(models.Model):

    name = models.CharField(max_length=200)

    description = models.TextField()

    url = models.URLField()

    image = models.URLField()

    price = models.FloatField()

    availability = models.CharField(max_length=20)

    power = models.CharField(max_length=20)

    voltage = models.CharField(max_length=20)
