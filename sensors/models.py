from django.db import models

class Sensor(models.Model):
    id = models.IntegerField(primary_key=True)
    station_id = models.IntegerField(blank=False)
    value = models.FloatField(blank=False)