from django.test import TestCase
from django.urls import reverse
from members.models import Member

class MemberTestCase(TestCase):
    def setUp(self):
        Member.objects.create(
                                first_name='Omkar',
                                last_name='Pathak',
                                mobile_number='80879966340',
                                email='test@gmail.com',
                    address='1234, Main Street, New York, NY 12345',
            medical_history='No medical history',
            admitted_on='2019-01-01',
            registration_date='2019-01-01',
            registration_upto='2019-01-01',
            dob='2019-01-01',
            subscription_type='gym',
            subscription_period='1',
            amount='500',
            fee_status='paid',
            batch='morning',
        )



    


