from django.urls import path
from . import views

urlpatterns = [
    path('', views.mailing, name='mailing'),
    path('send-newsletter/', views.send_newsletter, name='send_newsletter'),
]
