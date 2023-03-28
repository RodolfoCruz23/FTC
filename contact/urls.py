from django.urls import path

from . import views

urlpatterns = [
    path('', views.ContactList.as_view(), name='contact_list'),
    path('view/<int:pk>', views.ContactView.as_view(), name='contact_view'),
    path('new', views.ContactCreate.as_view(), name='contact_new'),
    path('view/<int:pk>', views.ContactView.as_view(), name='contact_view'),
    path('edit/<int:pk>', views.ContactUpdate.as_view(), name='contact_edit'),
    path('delete/<int:pk>', views.ContactDelete.as_view(), name='contact_delete'),
]