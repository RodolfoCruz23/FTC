from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
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

class GalleryDisplayView(TemplateView):
    template_name = 'gallery_display.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Gallery.objects.all()
        return context

def gallery_display(request):
    galleries = Gallery.objects.all()
    context = {'object_list': galleries}
    return render(request, 'gallery_display.html', context)


