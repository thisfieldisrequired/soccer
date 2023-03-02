from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Player(models.Model):
    height = models.FloatField()
    name = models.CharField(max_length=64)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Game(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='game_at_home')
    home_team_points = models.IntegerField()
    rival_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='rival_game')
    rival_team_points = models.IntegerField()
    date = models.DateField()


class Stadium(models.Model):
    title = models.CharField()
    seats = models.IntegerField()
    field_width = models.FloatField()
    field_length = models.FloatField()
    history = models.TextField()

    class Meta:
        app_label = 'tournament'


class Coach(models.Model):
    name = models.CharField(max_length=48)
    experience = models.IntegerField()
    team = models.CharField()


class Hotel(models.Model):
    title = models.CharField()
    location = models.CharField()
    rating = models.FloatField()
    stars = models.IntegerField()

    class Meta:
        app_label = 'hotels'