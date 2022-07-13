from django.test import TestCase
from subscriptions.models import Subscription
from django.utils.crypto import get_random_string
import random


class TestSubscriptionsModel(TestCase):
    def setUp(self):
        self.test_name = get_random_string(20)
        self.test_description = get_random_string(200)
        self.test_price = float(random.randrange(0, 500))/100
        self.test_weight = float(random.randrange(0, 500))
        self.test_image_url = 'www.test-example.com'

        self.test_subscription = Subscription.objects.create(
            name=self.test_name, 
            description=self.test_description, 
            price= self.test_price, 
            weight= self.test_weight,
            image_url= self.test_image_url,)
        self.return_subscription = Subscription.objects.get(pk=self.test_subscription.id)
        
    def test_subscription_created(self):
        self.assertEqual(len(Subscription.objects.all()), 1)
        self.assertEqual(self.return_subscription, self.test_subscription)

    def test_subscription_object_has_correct_data(self):
        self.assertEqual(self.return_subscription.name, self.test_name)
        self.assertEqual(self.return_subscription.description, self.test_description)
        self.assertEqual(float(self.return_subscription.price), self.test_price)
        self.assertEqual(float(self.return_subscription.weight), self.test_weight)
        self.assertEqual(self.return_subscription.image_url, self.test_image_url)

