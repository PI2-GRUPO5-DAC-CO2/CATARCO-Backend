#!/bin/bash

sleep 8
python3 manage.py migrate
python3 manage.py migrate --run-syncdb
python3 manage.py test