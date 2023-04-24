from django.test import TestCase, Client
from django.urls import reverse
from .models import Instructor, PersonalizedWorkout, Trainer

class PersonalTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.instructor = Instructor.objects.create(
            name='John Doe',
            bio='Test Bio',
            certifications='Test Certifications',
            experience_years=5
        )
        self.workout = PersonalizedWorkout.objects.create(
            name='Test Workout',
            description='Test Description',
            price=10.99
        )
        self.trainer = Trainer.objects.create(
            name='Test Trainer',
            bio='Test Bio',
            certifications='Test Certifications',
            experience_years=5
        )
        self.trainer.personalized_workouts.add(self.workout)

    def test_instructor_list_view(self):
        response = self.client.get(reverse('personal:instructor_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'personal/instructor_list.html')
        self.assertContains(response, self.instructor.name)

    def test_instructor_detail_view(self):
        response = self.client.get(reverse('personal:instructor_detail', args=[self.instructor.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'personal/instructor_detail.html')
        self.assertContains(response, self.instructor.name)

    def test_custom_workout_view(self):
        response = self.client.get(reverse('personal:custom_workout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'personal/custom_workout.html')

class InstructorModelTest(TestCase):

    def setUp(self):
        self.instructor = Instructor.objects.create(
            name='John Doe',
            bio='Fitness instructor with 10 years of experience',
            certifications='ACE, NASM',
            experience_years=10
        )

    def test_str(self):
        self.assertEqual(str(self.instructor), 'John Doe')


class PersonalizedWorkoutModelTest(TestCase):

    def setUp(self):
        self.workout = PersonalizedWorkout.objects.create(
            name='Weightlifting 101',
            description='Learn the basics of weightlifting',
            price=29.99
        )

    def test_str(self):
        self.assertEqual(str(self.workout), 'Weightlifting 101')


class TrainerModelTest(TestCase):

    def setUp(self):
        self.trainer = Trainer.objects.create(
            name='Jane Smith',
            bio='Personal trainer with a passion for helping clients achieve their fitness goals',
            certifications='NASM, ACE',
            experience_years=5
        )

    def test_str(self):
        self.assertEqual(str(self.trainer), 'Jane Smith')

    def test_personalized_workouts(self):
        workout = PersonalizedWorkout.objects.create(
            name='Circuit Training',
            description='A high-intensity workout that combines strength training and cardio',
            price=39.99
        )
        self.trainer.personalized_workouts.add(workout)
        self.assertIn(workout, self.trainer.personalized_workouts.all())


class InstructorListViewTest(TestCase):

    def setUp(self):
        self.url = reverse('personal:instructor_list')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'personal/instructor_list.html')


class InstructorDetailViewTest(TestCase):

    def setUp(self):
        self.instructor = Instructor.objects.create(
            name='John Doe',
            bio='Fitness instructor with 10 years of experience',
            certifications='ACE, NASM',
            experience_years=10
        )
        self.url = reverse('personal:instructor_detail', args=[self.instructor.pk])

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'personal/instructor_detail.html')


class CustomWorkoutViewTest(TestCase):

    def setUp(self):
        self.url = reverse('personal:custom_workout')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'personal/custom_workout.html')
