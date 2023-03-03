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


class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    pages_count = models.IntegerField()
    genre = models.CharField(max_length=30)
    book_cost = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=30)
