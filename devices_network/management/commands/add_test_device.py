from django.core.management.base import BaseCommand
from devices_network.models import Device, Sensor, Actuator


class Command(BaseCommand):
    help = 'Add to database test device'

    def handle(self, *args, **options):
        device = Device.objects.create(name='test_device',
                                       description='test device: temperature, humidity and pressure sensor. LED to controll',
                                       status='Ready')
        Sensor.objects.create(name='Temperature',
                              value=0,
                              device=device,
                              )
        Sensor.objects.create(name='Pressure',
                              value=0,
                              device=device,
                              )
        Sensor.objects.create(name='Humidity',
                              value=0,
                              device=device,
                              )
        Actuator.objects.create(name='LED',
                                value=0,
                                device=device)

