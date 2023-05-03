from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class MembershipTestCase(TestCase):
    def setUp(self):
        pass

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/membership/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('membership'))
        self.assertEqual(resp.status_code, 200)