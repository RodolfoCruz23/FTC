from django.test import TestCase
from books.models import Book
from django.urls import reverse

#  Test the views.py file

#Test BookList view
class BookListTest(TestCase):
    def setUp(self):
        Book.objects.create(name='The Great Gatsby', pages=200)
        Book.objects.create(name='The Catcher in the Rye', pages=300)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/books/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('book_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('book_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'books/book_list.html')

    def test_delete_book(self):
        resp = self.client.get(reverse('book_delete', kwargs={'pk': 1}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'books/book_confirm_delete.html')

    def  test_update_book(self):
        resp = self.client.get(reverse('book_edit', kwargs={'pk': 1}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'books/book_form.html')









