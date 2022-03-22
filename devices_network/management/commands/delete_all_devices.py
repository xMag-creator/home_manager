from django.core.management.base import BaseCommand
from devices_network.models import Device, Sensor, Actuator


class Command(BaseCommand):
    help = 'Delete all devices from database'

    def handle(self, *args, **options):
        Sensor.objects.all().delete()
        Actuator.objects.all().delete()
        Device.objects.all().delete()

