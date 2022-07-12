from django.test import TestCase
from django.urls import reverse
from django.core import mail
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


class TestSendNewsletterView(TestCase):
    def setUp(self):
        string = get_random_string(20)
        self.test_email = f'{string}@example.com'
        self.client.post(reverse('mailing'), {'email': self.test_email })

    def create_user(self, superuser):
        self.username = "test_user"
        self.password = User.objects.make_random_password()
        user, created = User.objects.get_or_create(username=self.username)
        user.set_password(self.password)
        user.is_staff = True
        user.is_superuser = superuser
        user.is_active = True
        user.save()
        self.user = user
    
    def test_url_exists_at_desired_location(self):
        self.create_user(True)
        self.client.login(username=self.username, password=self.password)
        response = self.client.get('/mailing/send-newsletter/')
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        self.create_user(True)
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('send_newsletter'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.create_user(True)
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('send_newsletter'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mailing/send_newsletter.html')

    def test_edit_title_returns_correct_data(self):
        self.create_user(True)
        self.client.login(username=self.username, password=self.password, email="test@example.com")
        string = get_random_string(20)

        response = self.client.post(
            reverse('send_newsletter'), 
            {'subject': string, 'message': string,})
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, string)

    def test_send_newsletter_redirects_non_superuser(self):
        string = get_random_string(20)
        self.create_user(False)
        self.client.login(username=self.username, password=self.password)

        response = self.client.post(
            reverse('send_newsletter',), 
            {'subject': string, 'message': string,})

        self.assertRedirects(response, '/', status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

    def test_send_newsletter_redirects_if_not_logged_in(self):
        string = get_random_string(20)

        response = self.client.post(
            reverse('send_newsletter',), 
            {'subject': string, 'message': string,})

        self.assertRedirects(response, '/accounts/login/?next=/mailing/send-newsletter/', status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)
