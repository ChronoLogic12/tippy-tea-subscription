from django.urls import path
from . import views
# from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('create-checkout-session/', views.create_checkout_session, name='create-checkout-session'),
    path('create-portal-session/', views.customer_portal, name='customer-portal'),
    path('webhook/', views.webhook_received, name='webhook-received'),
    path('success/', views.success, name='checkout-success'),
    path('cancel/', views.cancel, name='checkout-cancel'),
    # path('wh/', webhook, name='webhook'),
    ]