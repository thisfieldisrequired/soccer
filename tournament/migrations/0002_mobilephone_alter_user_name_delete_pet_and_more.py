# Generated by Django 4.1.7 on 2023-03-06 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MobilePhone',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='Pet',
        ),
        migrations.AddField(
            model_name='mobilephone',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='myphone', to='tournament.user'),
        ),
    ]
