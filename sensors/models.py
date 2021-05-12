from django.db import models

class Sensor(models.Model):
    station_id = models.IntegerField(blank=False)
    sensor_id = models.IntegerField(blank=False)
    value = models.FloatField(blank=False)