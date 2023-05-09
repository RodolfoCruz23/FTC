from django.test import TestCase, Client
from django.urls import reverse
from gallery.models import Gallery


class GalleryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Gallery.objects.create(name='Test Gallery', pages=5)

    def test_name_label(self):
        gallery = Gallery.objects.get(id=1)
        field_label = gallery._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_pages_label(self):
        gallery = Gallery.objects.get(id=1)
        field_label = gallery._meta.get_field('pages').verbose_name
        self.assertEquals(field_label, 'pages')

    def test_name_max_length(self):
        gallery = Gallery.objects.get(id=1)
        max_length = gallery._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)


class GalleryViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Gallery.objects.create(name='Test Gallery', pages=5)

    def setUp(self):
        self.gallery = Gallery.objects.create(name='Test Gallery', pages=10)


    def test_gallery_detail_view(self):
        gallery = Gallery.objects.create(name='Test Gallery', pages=5)
        response = self.client.get(reverse('gallery_view', args=[gallery.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery/gallery_detail.html')


class GalleryCreateViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_create_gallery(self):
        response = self.client.post(reverse('gallery_new'), {
            'name': 'New Gallery',
            'pages': 10,
            'image': ''
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Gallery.objects.count(), 1)


class GalleryUpdateViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Gallery.objects.create(name='Test Gallery', pages=5)

    def test_update_gallery(self):
        response = self.client.post(reverse('gallery_edit', args=[1]), {
            'name': 'Updated Gallery',
            'pages': 7,
            'image': ''
        })
        self.assertEqual(response.status_code, 302)
        gallery = Gallery.objects.get(id=1)
        self.assertEqual(gallery.name, 'Updated Gallery')
        self.assertEqual(gallery.pages, 7)


class GalleryDeleteViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Gallery.objects.create(name='Test Gallery', pages=5)

    def test_delete_gallery(self):
        response = self.client.post(reverse('gallery_delete', args=[1]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Gallery.objects.count(), 0)