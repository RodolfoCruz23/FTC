from django.test import TestCase
from django.urls import reverse
from gallery.models import Gallery


class GalleryTests(TestCase):
    def setUp(self):
        self.gallery = Gallery.objects.create(
            name='Test Gallery',
            pages=10
        )

    def test_gallery_list_view(self):
        response = self.client.get(reverse('gallery_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.gallery.name)

    def test_gallery_detail_view(self):
        response = self.client.get(reverse('gallery_view', kwargs={'pk': self.gallery.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.gallery.name)

    def test_gallery_create_view(self):
        data = {
            'name': 'New Gallery',
            'pages': 5
        }
        response = self.client.post(reverse('gallery_new'), data=data)
        self.assertEqual(response.status_code, 302)
        gallery = Gallery.objects.get(name='New Gallery')
        self.assertEqual(gallery.pages, 5)

    def test_gallery_update_view(self):
        data = {
            'name': 'Updated Gallery',
            'pages': 15
        }
        response = self.client.post(reverse('gallery_edit', kwargs={'pk': self.gallery.pk}), data=data)
        self.assertEqual(response.status_code, 302)
        gallery = Gallery.objects.get(pk=self.gallery.pk)
        self.assertEqual(gallery.name, 'Updated Gallery')
        self.assertEqual(gallery.pages, 15)

    def test_gallery_delete_view(self):
        response = self.client.post(reverse('gallery_delete', kwargs={'pk': self.gallery.pk}))
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Gallery.DoesNotExist):
            Gallery.objects.get(pk=self.gallery.pk)