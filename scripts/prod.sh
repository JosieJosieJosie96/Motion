#!/bin/sh

python manage.py runserver 0:8000
python manage.py migrate
python manage.py makemigrations