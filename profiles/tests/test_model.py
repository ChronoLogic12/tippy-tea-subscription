from django.shortcuts import get_object_or_404
from django.test import TestCase
from profiles.models import Profile, User
from profiles.forms import ProfileForm
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string

from profiles.views import *

class TestProfileModel(TestCase):
    def setUp(self):
        self.test_full_name = get_random_string(20)
        self.test_email = f'{self.test_full_name}@example.com'
        self.user = User.objects.create_user(username='test_user', password='testpassword')
        self.client.login(username='test_user', password='testpassword')
        self.profile = get_object_or_404(Profile, user=self.user)
        form = ProfileForm({'full_name': self.test_full_name, 'email': self.test_email, }, instance=self.profile)
        form.save()

    def test_profile_created(self):
        user = self.user
        self.assertEqual(user.username, "test_user")
        self.assertEqual(self.profile.full_name, self.test_full_name)
        self.assertEqual(self.profile.email, self.test_email)

