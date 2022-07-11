from django.test import TestCase
from mailing.models import Mailing
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User


class TestMailingModel(TestCase):
    def setUp(self):
        string = get_random_string(20)
        self.test_email = 'test@example.com'
        self.email = Mailing.objects.create(email=f'{string}@example.com')
        
    def test_email_added(self):
        self.assertEqual(len(Mailing.objects.all()), 1)
        return_email = Mailing.objects.get(email=self.email)
        self.assertEqual(return_email, self.email)
    

