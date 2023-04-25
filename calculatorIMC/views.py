from django.http import HttpResponse
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from calculatorIMC.models import CalculatorIMC


class CalculatorIMCView(DetailView):
    model = CalculatorIMC


class CalculatorIMCCreate(CreateView):
    model = CalculatorIMC
    fields = ['height', 'weight', 'imc']
    success_url = reverse_lazy('calculatorIMC_form')


class CalculatorIMCUpdate(UpdateView):
    model = CalculatorIMC
    fields = ['height', 'weight', 'imc']
    success_url = reverse_lazy('calculatorIMC_form')
