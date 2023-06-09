from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

from .models import *
from .utils import Calendar

def index(request):
    return HttpResponse("Hello, world!")

class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendario/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        calendario = Calendar(d.year, d.month)

        # Get the events for the current month
        events = Event.objects.filter(
            start_time__year=d.year,
            start_time__month=d.month
        )

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = calendario.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['events'] = events
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()