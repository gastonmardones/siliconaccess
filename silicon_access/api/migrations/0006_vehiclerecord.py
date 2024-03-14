# Generated by Django 4.2.11 on 2024-03-14 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_colour_vehicle_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y hora de ingreso')),
                ('exit_datetime', models.DateTimeField(blank=True, null=True, verbose_name='Fecha y hora de salida')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_records', to='api.vehicle')),
            ],
            options={
                'verbose_name': 'Registro de ingreso',
                'verbose_name_plural': 'Registro de ingresos',
            },
        ),
    ]