from django.db import models
from django.contrib.auth.models import User

class Mailing(models.Model):
    email = models.EmailField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.email
