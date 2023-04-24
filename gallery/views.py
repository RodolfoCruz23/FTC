from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from gallery.models import Gallery

class GalleryList(ListView):
    model = Gallery

class GalleryView(DetailView):
    model = Gallery

class GalleryCreate(CreateView):
    model = Gallery
    fields = ['name', 'pages', 'image']
    success_url = reverse_lazy('gallery_list')

class GalleryUpdate(UpdateView):
    model = Gallery
    fields = ['name', 'pages', 'image']
    success_url = reverse_lazy('gallery_list')

class GalleryDelete(DeleteView):
    model = Gallery
    success_url = reverse_lazy('gallery_list')


