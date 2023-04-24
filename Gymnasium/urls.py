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

from Gym import views
from Gym.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.about, name='contact'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('notifications/', include('notifications.urls')),
    path('reports/', include('reports.urls')),
    path('login', include('accounts.urls')),
    path('books/', include('books.urls')),
    path('contact/', include('contact.urls')),
    path('schedules/', include('schedules.urls')),
    path('', include('personal.urls')),
    path('', include('photo.urls')),
    path('gallery/', include('gallery.urls')),
]


