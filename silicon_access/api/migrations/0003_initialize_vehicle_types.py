from django.db import migrations, models


def initialize_vehicle_types(apps, schema_editor):
    """
    Inicializa una lista de tipos de vehículos
    """

    VehicleType = apps.get_model('api', 'VehicleType')
    vehicle_types_list = ['Auto', 'Camioneta', 'Moto', 'Bicicleta', 'Yate', 'Velero']
    for vehicle_type in vehicle_types_list:
        VehicleType.objects.get_or_create(name=vehicle_type)


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0002_vehicle'),
    ]

    operations = [
        migrations.RunPython(initialize_vehicle_types),
    ]
