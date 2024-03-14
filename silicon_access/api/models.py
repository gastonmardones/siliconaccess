from django.db import models


class VehicleType(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tipo de vehículo"
        verbose_name_plural = "Tipo de vehículos"
        app_label = "api"


class Vehicle(models.Model):
    ROLE_CHOICES = [('owner', 'Propietario'), ('guest', 'Invitado')]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='guest')
    type = models.ForeignKey(VehicleType, related_name='vehicles', on_delete=models.CASCADE)
    brand = models.CharField(verbose_name='Marca', max_length=64)
    model = models.CharField(verbose_name='Modelo', max_length=64)
    color = models.CharField(verbose_name='Color', max_length=64)
    license = models.CharField(verbose_name='Patente', max_length=64)
    insurance = models.CharField(verbose_name='Aseguradora', max_length=64)
    insurance_expiration = models.DateField(verbose_name='Expiración póliza')

    def __str__(self):
        return f"{self.type}: {self.brand} {self.model}. Patente: {self.license}"

    class Meta:
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"
        app_label = "api"


class VehicleRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name="vehicle_records", on_delete=models.CASCADE)
    entry_datetime = models.DateTimeField(verbose_name='Fecha y hora de ingreso', auto_now_add=True)
    exit_datetime = models.DateTimeField(verbose_name='Fecha y hora de salida', null=True, blank=True)

    def __str__(self):
        entry_str = self.entry_datetime.strftime('%Y-%m-%d %H:%M:%S')
        exit_str = self.exit_datetime.strftime('%Y-%m-%d %H:%M:%S') if self.exit_datetime else "N/A"
        return f"{self.vehicle} - Ingreso: {entry_str} - Egreso: {exit_str}"

    class Meta:
        verbose_name = "Registro de ingreso"
        verbose_name_plural = "Registro de ingresos"
        app_label = "api"
