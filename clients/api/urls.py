from django.urls import path
from . import viewsets

app_name = 'clients_api'


urlpatterns = [
    path('clientContact/', viewsets.client_contact, name='client_contact'),

]