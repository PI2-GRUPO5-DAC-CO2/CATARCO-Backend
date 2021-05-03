from django.db import models

class Sensor(models.Model):
    sensor_id: models.IntegerField(unique=True)
    station_id: models.IntegerField()
    value: models.IntegerField()