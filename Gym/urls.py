from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('horarios/', views.about, name='horarios'),
    path('servicios/', views.about, name='servicios'),
    path('contact/', views.contact, name='contact'),
    path('planes/', views.contact, name='planes'),
]