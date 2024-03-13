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
    type = models.ForeignKey(VehicleType, related_name='vehicles', on_delete=models.CASCADE)
    brand = models.CharField(verbose_name='Marca', max_length=64)
    model = models.CharField(verbose_name='Modelo', max_length=64)
    colour = models.CharField(verbose_name='Color', max_length=64)
    license = models.CharField(verbose_name='Patente', max_length=64)
    insurance = models.CharField(verbose_name='Aseguradora', max_length=64)
    insurance_expiration = models.DateField(verbose_name='Expiración póliza')

    def __str__(self):
        return f"{self.type}: {self.brand} {self.model}. Patente: {self.license}"

    class Meta:
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"
        app_label = "api"
