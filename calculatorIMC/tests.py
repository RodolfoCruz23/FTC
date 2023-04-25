from django.test import TestCase
from django.urls import reverse
from calculatorIMC.models import CalculatorIMC


# Create your tests here.
class ContactTestCase(TestCase):
    def setUp(self):
        CalculatorIMC.objects.create(
            height=1.80,
            weight=80,
            imc=24.69)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/calculatorIMC/')
        self.assertEqual(resp.status_code, 200)


    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('calculatorIMC'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'calculatorIMC/calculatorIMC.html')

    def test_calculate_imc(self):
        resp = self.client.get(reverse('calculatorIMC'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'calculatorIMC/calculatorIMC.html')
        self.assertEqual(resp.context['imc'], 24.69)
