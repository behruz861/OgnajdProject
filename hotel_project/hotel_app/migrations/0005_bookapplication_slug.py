# Generated by Django 5.0.1 on 2024-01-15 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0004_room_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookapplication',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
