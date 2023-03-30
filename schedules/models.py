from django.db import models
from django.urls import reverse

class Schedule(models.Model):
    name = models.CharField(max_length=200)
    instructor = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('schedule_edit', kwargs={'pk': self.pk})