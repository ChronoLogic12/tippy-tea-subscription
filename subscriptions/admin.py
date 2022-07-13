from django.contrib import admin
from .models import Subscription


class SubscriptionsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
        'weight',
        'image_url',
    )

admin.site.register(Subscription, SubscriptionsAdmin)
