from .models import Device, Sensor
from .serializers import DeviceSerializer, SensorSerializer
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
        print(sensor)
        return sensor
