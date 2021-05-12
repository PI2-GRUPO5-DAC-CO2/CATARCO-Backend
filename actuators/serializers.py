from rest_framework import serializers
from .models import Actuator


class ActuatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actuator
        fields = '__all__'
