# Generated by Django 5.1.6 on 2025-02-11 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_casa', models.CharField(max_length=100)),
                ('time_fora', models.CharField(max_length=100)),
                ('data', models.DateTimeField()),
                ('odds_casa', models.FloatField()),
                ('odds_fora', models.FloatField()),
            ],
        ),
    ]
