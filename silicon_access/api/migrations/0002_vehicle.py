# Generated by Django 5.0.3 on 2024-03-12 00:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=64, verbose_name='Marca')),
                ('model', models.CharField(max_length=64, verbose_name='Modelo')),
                ('colour', models.CharField(max_length=64, verbose_name='Color')),
                ('license', models.CharField(max_length=64, verbose_name='Patente')),
                ('insurance', models.CharField(max_length=64, verbose_name='Aseguradora')),
                ('insurance_expiration', models.DateField(verbose_name='Expiración póliza')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='api.vehicletype')),
            ],
            options={
                'verbose_name': 'Vehículo',
                'verbose_name_plural': 'Vehículos',
            },
        ),
    ]
