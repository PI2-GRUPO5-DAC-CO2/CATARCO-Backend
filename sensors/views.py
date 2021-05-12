from .models import Sensor
from rest_framework import viewsets, permissions
from sensors.serializers import SensorSerializer


class SensorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sensors to be viewed or edited.
    """
    queryset = Sensor.objects.all().order_by('sensor_id')
    serializer_class = SensorSerializer
    permission_classes = [permissions.AllowAny]