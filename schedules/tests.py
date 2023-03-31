from django.test import TestCase
from django.urls import reverse
from schedules.models import Schedule

# Create your tests here.
class ScheduleTestCase(TestCase):
    def setUp(self):
        Schedule.objects.create(
            name='Schedule 1',
            instructor='Instructor 1',
            start_date='2019-01-01',
            end_date='2019-01-01',
            start_time='10:00:00',
            end_time='11:00:00',
        )
        
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/schedules/')
        self.assertEqual(resp.status_code, 200)
        
    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('schedule_list'))
        self.assertEqual(resp.status_code, 200)
        
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('schedule_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'schedules/schedule_list.html')
        
    def test_delete_schedule(self):
        resp = self.client.get(reverse('schedule_delete', kwargs={'pk': 1}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'schedules/schedule_confirm_delete.html')
        
    def test_update_schedule(self):
        resp = self.client.get(reverse('schedule_edit', kwargs={'pk': 1}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'schedules/schedule_form.html')
        
    def test_create_schedule(self):
        resp = self.client.get(reverse('schedule_new'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'schedules/schedule_form.html')
        
        
            
