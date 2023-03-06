from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()

class MobilePhone(models.Model):
    id = models.IntegerField(primary_key=True)
    phone = models.CharField(max_length=10)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='myphone')


class Chat(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    users = models.ManyToManyField(User, related_name='chats')