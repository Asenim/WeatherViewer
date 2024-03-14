#!/bin/sh

# shellcheck disable=SC2164
cd WeatherViewerProject
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
