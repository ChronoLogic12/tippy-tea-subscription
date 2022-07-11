from django.test import TestCase
from django.urls import reverse
from django.utils.crypto import get_random_string

from mailing.models import Mailing
from mailing.forms import MailingForm

from django.contrib.auth.models import User
from django.test.client import Client

class TestMailingView(TestCase):
    def test_url_exists_at_desired_location(self):
        response = self.client.get('/mailing/')
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('mailing'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('mailing'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mailing/mailing.html')


class TestUpdateMailingView(TestCase):
    def setUp(self):
        string = get_random_string(20)
        self.test_email = f'{string}@example.com'

    def test_add_new_email_returns_correct_data(self):
        response = self.client.post(reverse('mailing'), {'email': self.test_email })
        email_added = Mailing.objects.filter(email=self.test_email).exists()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(email_added, True)
