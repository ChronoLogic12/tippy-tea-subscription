from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):

    readonly_fields = ('order_number', 'product', 'user')

    list_display = ('order_number', 'product', 'user')

    ordering = ('product',)

admin.site.register(Order, OrderAdmin)