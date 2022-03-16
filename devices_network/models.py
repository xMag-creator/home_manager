from django.db import models


# Create your models here.
class Sensor(models.Model):
    name = models.CharField(max_length=128, unique=True)
    value = models.FloatField()


class Actuator(models.Model):
    name = models.CharField(max_length=128, unique=True)
    value = models.FloatField()


class Device(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=128)
    sensors = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    actuators = models.ForeignKey(Actuator, on_delete=models.CASCADE)

