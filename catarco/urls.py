from django.urls import include, path
from rest_framework import routers
from users.views import UserViewSet
from sensors.views import SensorViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'sensors', SensorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]