# Generated by Django 2.0.4 on 2018-05-18 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('belt_users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logusers',
            name='trip_palns',
        ),
        migrations.RemoveField(
            model_name='logusers',
            name='trips',
        ),
        migrations.DeleteModel(
            name='trip',
        ),
    ]
