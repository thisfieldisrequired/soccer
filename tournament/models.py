from django.db import models


class DayWeateher(models.Model):
    date = models.DateField()
    precipitation = models.FloatField()
    temperature = models.FloatField()
    was_raining = models.BooleanField()
