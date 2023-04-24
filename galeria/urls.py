from django.urls import path
from .views import ImageList

urlpatterns = [
    path('', ImageList.as_view(), name='image_list'),
]