from django.test import TestCase
from django.urls import reverse
from contact.models import Contact

# Create your tests here.

class ContactTestCase(TestCase):
    def setUp(self):
        Contact.objects.create(
            name='Robert',
            email='robert@gmail.com',
            phone='1234567890',
            address='1234, Main Street, New York, NY 12345')
        
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/contact/')
        self.assertEqual(resp.status_code, 200)
        
    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('contact_list'))
        self.assertEqual(resp.status_code, 200)
        
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('contact_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'contact/contact_list.html')
        
    def test_delete_contact(self):
        resp = self.client.get(reverse('contact_delete', kwargs={'pk': 1}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'contact/contact_confirm_delete.html')
        
    def test_update_contact(self):
        resp = self.client.get(reverse('contact_edit', kwargs={'pk': 1}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'contact/contact_form.html')
        
    def test_create_contact(self):
        resp = self.client.get(reverse('contact_new'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'contact/contact_form.html')
                         
                         