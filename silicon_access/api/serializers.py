from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import serializers

from .models import Vehicle, VehicleType, VehicleRecord


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    type = VehicleTypeSerializer()

    def validate(self, data):
        insurance_expiration = data.get('insurance_expiration')
        if insurance_expiration and timezone.now().date() >= insurance_expiration:
            raise serializers.ValidationError(
                {'insurance_expiration': 'La fecha de expiración del seguro está vencida.'})

        return data

    class Meta:
        model = Vehicle
        fields = '__all__'


class VehicleRecordSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()

    def validate(self, data):
        entry_datetime = data.get('entry_datetime')
        exit_datetime = data.get('exit_datetime')
        try:
            # Intenta formatear el valor utilizando el formato especificado
            if entry_datetime:
                entry_datetime.strftime('%Y-%m-%d %H:%M:%S')
            if exit_datetime:
                exit_datetime.strftime('%Y-%m-%d %H:%M:%S')
        except ValueError:
            raise serializers.ValidationError(
                'El formato de fecha y hora debe ser YYYY-MM-DD HH:MM:SS',
                code='invalid_datetime_format'
            )

        if exit_datetime and entry_datetime >= exit_datetime:
            raise serializers.ValidationError(
                {'exit_datetime': 'La fecha de salida debe ser posterior a la fecha de entrada.'})

        return data

    class Meta:
        model = VehicleRecord
        fields = '__all__'
