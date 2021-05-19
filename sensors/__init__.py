from django.conf import settings
from . import subscriber

if settings.RUNSERVER:
    print("Initing sensors subscriber")
    subscriber.run()