from .models import Actuator
from rest_framework import serializers


class ActuatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actuator
        fields = '__all__'
