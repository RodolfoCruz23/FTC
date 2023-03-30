from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from contact.models import Contact

class ContactList(ListView):
    model = Contact

class ContactView(DetailView):
    model = Contact

class ContactCreate(CreateView):
    model = Contact
    fields = ['name', 'email', 'phone', 'address']
    success_url = reverse_lazy('contact_list')

class ContactUpdate(UpdateView):
    model = Contact
    fields = ['name', 'email', 'phone', 'address']
    success_url = reverse_lazy('contact_list')

class ContactDelete(DeleteView):
    model = Contact
    success_url = reverse_lazy('book_list')