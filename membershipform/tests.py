from django.test import TestCase
from .models import Cliente
from django.urls import reverse

class ClienteModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Cliente.objects.create(
            nombre='John Doe',
            correo_electronico='john@example.com',
            direccion='123 Main St',
            telefono='555-1234'
        )

    def test_nombre_label(self):
        cliente = Cliente.objects.get(id=1)
        field_label = cliente._meta.get_field('nombre').verbose_name
        self.assertEqual(field_label, 'nombre')

    def test_correo_electronico_label(self):
        cliente = Cliente.objects.get(id=1)
        field_label = cliente._meta.get_field('correo_electronico').verbose_name
        self.assertEqual(field_label, 'correo electronico')

    def test_direccion_label(self):
        cliente = Cliente.objects.get(id=1)
        field_label = cliente._meta.get_field('direccion').verbose_name
        self.assertEqual(field_label, 'direccion')

    def test_telefono_label(self):
        cliente = Cliente.objects.get(id=1)
        field_label = cliente._meta.get_field('telefono').verbose_name
        self.assertEqual(field_label, 'telefono')

    def test_fecha_solicitud_label(self):
        cliente = Cliente.objects.get(id=1)
        field_label = cliente._meta.get_field('fecha_solicitud').verbose_name
        self.assertEqual(field_label, 'fecha solicitud')

    def test_nombre_max_length(self):
        cliente = Cliente.objects.get(id=1)
        max_length = cliente._meta.get_field('nombre').max_length
        self.assertEqual(max_length, 100)

    def test_direccion_max_length(self):
        cliente = Cliente.objects.get(id=1)
        max_length = cliente._meta.get_field('direccion').max_length
        self.assertEqual(max_length, 200)

    def test_telefono_max_length(self):
        cliente = Cliente.objects.get(id=1)
        max_length = cliente._meta.get_field('telefono').max_length
        self.assertEqual(max_length, 20)
