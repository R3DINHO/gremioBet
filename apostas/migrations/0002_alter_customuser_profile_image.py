# Generated by Django 5.1.6 on 2025-02-22 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apostas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_image',
            field=models.CharField(default='img/fotosPerfil/default.png', max_length=255),
        ),
    ]
