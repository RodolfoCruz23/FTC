from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from schedules.models import Schedule

class ScheduleList(ListView):
    model = Schedule

class ScheduleView(DetailView):
    model = Schedule

class ScheduleCreate(CreateView):
    model = Schedule
    fields = ['name', 'instructor', 'start_date', 'end_date', 'start_time', 'end_time']
    success_url = reverse_lazy('schedule_list')

class ScheduleUpdate(UpdateView):
    model = Schedule
    fields = ['name', 'instructor', 'start_date', 'end_date', 'start_time', 'end_time']
    success_url = reverse_lazy('shedule_list')

class ScheduleDelete(DeleteView):
    model = Schedule
    success_url = reverse_lazy('schedule_list')