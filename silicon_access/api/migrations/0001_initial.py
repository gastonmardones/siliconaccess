# Generated by Django 5.0.3 on 2024-03-12 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Tipo de vehículo',
                'verbose_name_plural': 'Tipo de vehículos',
            },
        ),
    ]
