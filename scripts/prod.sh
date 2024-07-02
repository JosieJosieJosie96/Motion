#!/bin/sh

python manage.py migrate
python manage.py makemigrations
gunicorn -w 4 -b 0.0.0.0:8000 project.wsgi:application # This is the WSGI_APPLICATION from settings.py. Here its a : IMPORTANT
