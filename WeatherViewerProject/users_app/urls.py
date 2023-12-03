from django.urls import path
from users_app.views import *

urlpatterns = [
    path('login/', user_authorization, name='user_authorization'),
    path('registration/', user_registration, name='user_registration')
]
