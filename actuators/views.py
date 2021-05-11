from actuators.serializers import ActuatorSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Actuator
from . import publisher
import json


class ActuatorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows actuators to be viewed or edited.
    """
    queryset = Actuator.objects.all()
    serializer_class = ActuatorSerializer
    permission_classes = [permissions.AllowAny]


@api_view(['POST', 'PUT'])
def actuator_publisher(request):
    data = JSONParser().parse(request)

    try:
        actuator = Actuator.objects.get(
            id=data['id'], actuator_id=data['actuator_id']
        )
    except Actuator.DoesNotExist:
        return JsonResponse({"error": "Atuador não encontrado"}, status=status.HTTP_404_NOT_FOUND)

    actuator = None
    if data['id'] == 1 : actuator = "sistema"
    else: actuator = "ventilador"

    publisher.run(
        [f"/CATARCO/atuador/{actuator}_w", {
            f'{actuator}': data['value'],
            'estacao_id': 1,
            'atuador_id': data['actuator_id']
        }
    ])
    Actuator.objects.filter(id=data['id'], actuator_id=data['actuator_id']).update(
        value=data['value']
    )
    return JsonResponse({"message": "Atuador atualizado!"})
