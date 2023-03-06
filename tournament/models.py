from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=33)


class Pet(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=7)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mypets')
