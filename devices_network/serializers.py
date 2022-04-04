from rest_framework import serializers
from .models import Device, Sensor, Actuator


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['name', 'value']


class ActuatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actuator
        fields = ['name', 'value']


class DeviceSerializer(serializers.ModelSerializer):
    sensors = SensorSerializer(many=True)
    actuators = ActuatorSerializer(many=True)

    class Meta:
        model = Device
        fields = ['name', 'description', 'status', 'sensors', 'actuators']
        read_only_fields = ('name', )
