from django.test import TestCase, Client
from django.urls import reverse
from . import views

class MapViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.map_url = reverse('map')

    def test_map_view(self):
        response = self.client.get(self.map_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'maps/map.html')