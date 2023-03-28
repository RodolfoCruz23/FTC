from django.urls import path

from . import views

urlpatterns = [
    path('', views.ScheduleList.as_view(), name='schedule_list'),
    path('view/<int:pk>', views.ScheduleView.as_view(), name='schedule_view'),
    path('new', views.ScheduleCreate.as_view(), name='schedule_new'),
    path('view/<int:pk>', views.ScheduleView.as_view(), name='schedule_view'),
    path('edit/<int:pk>', views.ScheduleUpdate.as_view(), name='schedule_edit'),
    path('delete/<int:pk>', views.ScheduleDelete.as_view(), name='schedule_delete'),
]