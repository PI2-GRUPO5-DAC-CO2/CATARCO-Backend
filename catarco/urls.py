from django.urls import include, path
from rest_framework import routers
from users.views import UserViewSet
from sensors.views import SensorViewSet
from actuators.views import ActuatorViewSet, actuator_publisher

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'sensors', SensorViewSet)
router.register(r'actuators', ActuatorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('actuators/publish/', actuator_publisher),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]