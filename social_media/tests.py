from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class SocialMediaTestCase(TestCase):
    def setUp(self):
        pass

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/social_media/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('social_media'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('social_media'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'social_media/social_media.html')
