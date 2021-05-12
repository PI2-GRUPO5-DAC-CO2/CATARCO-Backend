#!/bin/bash

sleep 8
python3 manage.py migrate
python3 manage.py migrate --run-syncdb

USER=$(echo "from django.contrib.auth.models import User; u = User.objects.filter(username='$ADMIN_USER').first(); print(u)" | python manage.py shell)
if [ "$USER" = "$ADMIN_USER" ]; then
    echo "Database appears to contain a superuser, skipping superuser creation..."
else
    echo "from django.contrib.auth.models import User; User.objects.create_superuser('$ADMIN_USER', '$ADMIN_EMAIL', '$ADMIN_PASS')" | python manage.py shell
fi;

python3 manage.py runserver --noreload 0.0.0.0:8000