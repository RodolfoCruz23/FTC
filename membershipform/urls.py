from django.urls import path
from . import views

app_name = 'membershipform'

urlpatterns = [
    path('solicitud/', views.solicitud_membresia, name='solicitud_membresia'),
    path('solicitud-exitosa/', views.solicitud_exitosa, name='solicitud_exitosa'),
]