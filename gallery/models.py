from django.db import models
from django.urls import reverse
from django.db.models.fields.files import ImageField


class CustomImageField(models.ImageField):
    def __init__(self, *args, manual_crop=None, **kwargs):
        self.manual_crop = manual_crop
        super().__init__(*args, **kwargs)

        
class Gallery(models.Model):
    name = models.CharField(max_length=200)
    pages = models.IntegerField()
    # field for image
    image = CustomImageField(blank=True, manual_crop="800x800")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('gallery_edit', kwargs={'pk': self.pk})
