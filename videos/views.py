from django.shortcuts import render
from .models import Video

def galeria_videos(request):
    videos = Video.objects.all()
    return render(request, 'videos/galeria_videos.html', {'videos': videos})