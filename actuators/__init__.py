from django.conf import settings
from . import subscriber

if settings.RUNSERVER:
    print("Initing actuators subscriber")
    subscriber.run()