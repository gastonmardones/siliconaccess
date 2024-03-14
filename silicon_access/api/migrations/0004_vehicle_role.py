# Generated by Django 4.2.11 on 2024-03-14 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_initialize_vehicle_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='role',
            field=models.CharField(choices=[('owner', 'Propietario'), ('guest', 'Invitado')], default='guest', max_length=20),
        ),
    ]
