from django.urls import path
from . import views

app_name = 'calendario'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    # other URL patterns go here
]