# Generated by Django 4.1.7 on 2023-03-06 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=120)),
                ('country', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('runway_length', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=120)),
                ('model', models.CharField(max_length=120)),
                ('seats', models.IntegerField()),
                ('runway_min_lenght', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=120)),
                ('passengers_count', models.IntegerField()),
                ('from_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_airport', to='tournament.airport')),
                ('plane', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plane', to='tournament.plane')),
                ('to_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_airport', to='tournament.airport')),
            ],
        ),
    ]
