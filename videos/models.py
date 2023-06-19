from django.db import models
from embed_video.fields import EmbedVideoField

class Video(models.Model):
    titulo = models.CharField(max_length=100)
    url = EmbedVideoField()

    def __str__(self):
        return self.titulo