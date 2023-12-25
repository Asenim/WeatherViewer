from django.urls import path
from location_app.views import *


urlpatterns = [
    path('add/', weather_viewer_add, name='viewer_add'),
    path('user/', view_user_locations, name='user_locations'),
    path('delete/', weather_viewer_delete, name='viewer_delete')
]
