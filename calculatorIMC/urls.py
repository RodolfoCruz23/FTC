from django.urls import path
from . import views

app_name = 'calculatorIMC'

urlpatterns = [
    path('', views.calculate_bmi_view, name='calculate_bmi'),
]