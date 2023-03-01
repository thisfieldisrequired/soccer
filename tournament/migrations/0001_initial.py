# Generated by Django 4.1.7 on 2023-03-01 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.FloatField()),
                ('name', models.CharField(max_length=64)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.team')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_team_points', models.IntegerField()),
                ('rival_team_points', models.IntegerField()),
                ('date', models.DateField()),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_at_home', to='tournament.team')),
                ('rival_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rival_game', to='tournament.team')),
            ],
        ),
    ]
