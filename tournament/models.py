from django.db import models


class DayWeateher(models.Model):
    date = models.DateField()
    precipitation = models.FloatField()
    temperature = models.FloatField()
    was_raining = models.BooleanField()


class House(models.Model):
    apartments = models.IntegerField()
    house_number = models.IntegerField()
    street = models.CharField(max_length=64)
