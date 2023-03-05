from django.db import models


class Alien(models.Model):
    type = models.CharField(max_length=32)
    distance_to_galaxy = models.IntegerField()
    threat = models.IntegerField()
    speed = models.IntegerField()


class Weapon(models.Model):
    type = models.CharField(max_length=32)
    quantity = models.IntegerField()
    power = models.IntegerField()
    coverage_distance = models.IntegerField()
