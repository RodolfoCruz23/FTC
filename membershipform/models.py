from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre