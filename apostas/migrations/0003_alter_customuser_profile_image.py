# Generated by Django 5.1.6 on 2025-02-22 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apostas', '0002_alter_customuser_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_image',
            field=models.CharField(default='default.png', max_length=255),
        ),
    ]
