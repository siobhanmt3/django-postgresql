from django.db import models

# Create your models here.

class Inventory(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=100)
    identifier = models.CharField(max_length=10, null=True)


class Locations(models.Model):
    name = models.CharField(max_length=100)