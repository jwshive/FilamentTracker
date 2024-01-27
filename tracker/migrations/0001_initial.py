# Generated by Django 5.0.1 on 2024-01-27 18:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FilamentManufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Filament Manufacturer',
            },
        ),
        migrations.CreateModel(
            name='FilamentTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filament_type', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Filament Types',
            },
        ),
        migrations.CreateModel(
            name='PrintBeds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bed_type', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Bed Types',
            },
        ),
        migrations.CreateModel(
            name='Printers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('printer_name', models.CharField(max_length=255)),
                ('printer_make', models.CharField(max_length=255)),
                ('printer_model', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Printers',
            },
        ),
        migrations.CreateModel(
            name='FilamentConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flow_rate', models.DecimalField(decimal_places=3, max_digits=5)),
                ('pressure_advance', models.DecimalField(decimal_places=3, max_digits=5)),
                ('first_layer_temp', models.IntegerField(max_length=3)),
                ('other_layer_temp', models.IntegerField(max_length=3)),
                ('plate_temp', models.IntegerField(max_length=2)),
                ('max_volumetric_speed', models.DecimalField(decimal_places=3, max_digits=5)),
                ('filament_brand', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tracker.filamentmanufacturer')),
                ('filament_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tracker.filamenttypes')),
                ('bed_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tracker.printbeds')),
                ('printer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tracker.printers')),
            ],
            options={
                'verbose_name_plural': 'Filament Configurations',
            },
        ),
    ]
