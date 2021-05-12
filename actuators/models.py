from django.db import models

class Actuator(models.Model):
    station_id = models.IntegerField(blank=False)
    actuator_id = models.IntegerField(blank=False)
    value = models.IntegerField(blank=False)