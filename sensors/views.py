from .models import Sensor
from rest_framework import viewsets
from models.serializer import SensorSerializer

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorViewSet()