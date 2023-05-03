from django.db import models
from django.urls import reverse


class CalculatorIMC(models.Model):
    height = models.DecimalField(max_digits=3, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    imc = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.imc

    def get_absolute_url(self):
        return reverse('calculatorIMC', kwargs={'pk': self.pk})

    def calculate_imc(self):
        return self.weight / (self.height * self.height)
