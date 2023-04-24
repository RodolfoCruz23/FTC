from django.urls import path

from . import views
from .views import GalleryDisplayView

urlpatterns = [
    path('', views.GalleryList.as_view(), name='gallery_list'),
    path('view/<int:pk>', views.GalleryView.as_view(), name='gallery_view'),
    path('new', views.GalleryCreate.as_view(), name='gallery_new'),
    path('view/<int:pk>', views.GalleryView.as_view(), name='gallery_view'),
    path('edit/<int:pk>', views.GalleryUpdate.as_view(), name='gallery_edit'),
    path('delete/<int:pk>', views.GalleryDelete.as_view(), name='gallery_delete'),
    path('display/', views.gallery_display, name='gallery_display'),
]