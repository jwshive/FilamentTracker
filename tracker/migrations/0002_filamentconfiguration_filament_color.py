# Generated by Django 5.0.1 on 2024-01-27 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filamentconfiguration',
            name='filament_color',
            field=models.CharField(default='Black', max_length=255),
            preserve_default=False,
        ),
    ]