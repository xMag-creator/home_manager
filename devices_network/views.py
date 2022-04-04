from .models import Device, Sensor, Actuator
from .serializers import DeviceSerializer, SensorSerializer, ActuatorSerializer
from rest_framework import generics


class DeviceListView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = DeviceSerializer
    lookup_field = 'username'

    def get_object(self):
        name = self.kwargs["name"]
        device = generics.get_object_or_404(Device, name=name)
        print(device)

        return device

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class SensorRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def get_object(self):
        device_name = self.kwargs["device"]
        sensor_name = self.kwargs["sensor"]
        device = Device.objects.get(name=device_name)
        sensor = generics.get_object_or_404(Sensor, device_id=device.pk, name=sensor_name)

        return sensor


class ActuatorRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Actuator.objects.all()
    serializer_class = ActuatorSerializer

    def get_object(self):
        device_name = self.kwargs["device"]
        actuator_name = self.kwargs["actuator"]
        device = Device.objects.get(name=device_name)
        actuator = generics.get_object_or_404(Actuator, device_id=device.pk, name=actuator_name)
        print(actuator)
        return actuator
