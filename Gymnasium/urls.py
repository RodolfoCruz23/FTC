"""Gymnasium URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.urls import include

from Gym import views
from Gym.views import home
from maps.views import map_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('horarios/', views.horarios, name='horarios'),
    path('servicios/', views.servicios, name='servicios'),
    path('planes/', views.planes, name='planes'),
    path('contacto/', views.contacto, name='contacto'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),  # Add this line to include the URLs of the accounts app
    path('members/', include('members.urls')),
    path('notifications/', include('notifications.urls')),
    path('reports/', include('reports.urls')),
    path('login', include('accounts.urls')),
    path('books/', include('books.urls')),
    path('contact/', include('contact.urls')),
    path('schedules/', include('schedules.urls')),
    path('', include('personal.urls')),
    path('', include('photo.urls')),
    path('gallery/', include('gallery.urls', namespace='gallery')),
    path('calculatorIMC/', include('calculatorIMC.urls')),
    path('social_media/', include('social_media.urls')),
    path('membership/', include('membership.urls')),
    path('', include('calendario.urls')),
    path('calendario/', include('calendario.urls', namespace='calendar')),
    path('maps/', include('maps.urls', namespace='maps')),
    path('membershipform/', include('membershipform.urls')),
]


