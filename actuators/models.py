from django.db import models

class Actuator(models.Model):
    id = models.IntegerField(primary_key=True)
    actuator_id = models.IntegerField(blank=False)
    station_id = models.IntegerField(blank=False)
    value = models.IntegerField(blank=False)