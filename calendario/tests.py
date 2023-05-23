from datetime import date
from django.test import TestCase, RequestFactory
from django.urls import reverse
from .models import Event
from .views import CalendarView

class CalendarViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.url = reverse('calendar')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/calendar/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('calendar'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('calendar'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'calendario/calendar.html')