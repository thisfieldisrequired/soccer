from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=64)


class Game(models.Model):
    home_team = models.ForeignKey(Team, related_name='game_at_home', on_delete=models.CASCADE)
    home_team_points = models.IntegerField()
    rival_team = models.ForeignKey(Team, related_name='rival_game', on_delete=models.CASCADE)
    rival_team_points = models.IntegerField()
    date = models.DateField()

