from .models import Actuator
from rest_framework import viewsets, permissions
from actuators.serializers import ActuatorSerializer


class ActuatorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows actuators to be viewed or edited.
    """
    queryset = Actuator.objects.all()
    serializer_class = ActuatorSerializer
    permission_classes = [permissions.AllowAny]