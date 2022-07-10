from django.test import TestCase
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string

from profiles.models import Profile
from profiles.forms import ProfileForm

from django.contrib.auth.models import User
from django.test.client import Client


class TestProfileView(TestCase):
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
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        self.create_user(True)
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.create_user(True)
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')


class TestUpdateProfile(TestCase):
    def setUp(self):
        self.test_full_name = 'Joe Blogs'
        self.test_email = 'test@example.com'
        self.user = User.objects.create_user(username='test_user', password='testpassword')
        self.client.login(username='test_user', password='testpassword')
        self.profile = get_object_or_404(Profile, user=self.user)
        self.form = ProfileForm({'full_name': self.test_full_name, 'email': self.test_email, }, instance=self.profile)
        self.form.save()

    def test_edit_profile_name_returns_correct_data(self):
        string = get_random_string(20)
        response = self.client.post(reverse('profile'), {'full_name': string, 'email': self.test_email})
        self.profile = get_object_or_404(Profile, user=self.user)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.profile.full_name, string)


class TestDeleteProfile(TestCase):

    def setUp(self):
        self.test_full_name = get_random_string(20)
        self.test_email = f'{self.test_full_name}@example.com'
        self.user = User.objects.create_user(username='test_user', password='testpassword')
        self.client.login(username='test_user', password='testpassword')
        self.profile = get_object_or_404(Profile, user=self.user)
        self.form = ProfileForm({'full_name': self.test_full_name, 'email': self.test_email, }, instance=self.profile)
        self.form.save()

    def test_delete_profile_returns_correct_status_code(self):

        response = self.client.delete(reverse('delete_profile'))
        self.user = self.user if User.objects.filter(username='test_user') else None

        self.assertRedirects(response, '/', status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)
        self.assertEqual(self.user, None)


    def test_delete_profile_redirects_if_not_logged_in(self):
        self.client.logout()
        response = self.client.delete(reverse('delete_profile'))

        self.assertRedirects(response, '/accounts/login/?next=/profile/delete/', status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

