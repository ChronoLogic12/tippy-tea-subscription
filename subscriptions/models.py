from django.db import models


class Subscription(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=10000, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    weight = models.CharField(max_length=50, null=False, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name
