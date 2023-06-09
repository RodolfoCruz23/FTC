from django.urls import path
from .views import galeria_videos

app_name = 'videos'

urlpatterns = [
    path('', galeria_videos, name='galeria_videos'),
]