from django.urls import path
from location_app.views import *


urlpatterns = [
    path('find/', weather_viewer_find, name='viewer_find'),
    path('add/', weather_viewer_add, name='viewer_add')
]
