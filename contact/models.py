from django.db import models
from django.urls import reverse

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contact_edit', kwargs={'pk': self.pk})
