from rest_framework import serializers
from .models import Device, Sensor


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['name', 'value']


class DeviceSerializer(serializers.ModelSerializer):
    sensors = SensorSerializer(many=True)

    class Meta:
        model = Device
        fields = ['name', 'description', 'status', 'sensors']

    # def create(self, validated_data):
    #     sensors_data = validated_data.pop('sensor')

