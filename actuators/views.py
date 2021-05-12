from actuators.serializers import ActuatorSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Actuator
from . import publisher


class ActuatorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows actuators to be viewed or edited.
    """
    queryset = Actuator.objects.all()
    serializer_class = ActuatorSerializer
    permission_classes = [permissions.AllowAny]


@api_view(['PUT'])
def actuator_publisher(request):
    data = JSONParser().parse(request)

    try:
        actuator = Actuator.objects.get(
            station_id=data['estacao_id'],
            actuator_id=data['atuador_id']
        )
    except Actuator.DoesNotExist:
        return JsonResponse(
            {"error": "Atuador não encontrado"},
            status=status.HTTP_404_NOT_FOUND
        )

    actuator = None
    if data['atuador_id'] == 1 :
        actuator = "sistema"
    else:
        actuator = "ventilador"

    metrics = [f"/CATARCO/atuador/{actuator}_w",
        {
            'estacao_id': data['estacao_id'],
            'atuador_id': data['atuador_id'],
            f'{actuator}': data['valor']
        }
    ]
    publisher.run(metrics)
    
    return JsonResponse({"message": "Atuador atualizado!"})
