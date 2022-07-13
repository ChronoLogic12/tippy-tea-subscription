from django.test import TestCase
from django.urls import reverse

from subscriptions.models import Subscription

class TestSubscriptionsView(TestCase):
    def setUp(self):
        Subscription.objects.create(name="classic", description="test description", price=10.00, weight=10.00)
        Subscription.objects.create(name="large", description="test description", price=10.00, weight=10.00)
        Subscription.objects.create(name="discovery", description="test description", price=10.00, weight=10.00)
                        
    def test_url_exists_at_desired_location(self):
        response = self.client.get('/subscriptions/')
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('subscriptions'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('subscriptions'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'subscriptions/subscriptions.html')
