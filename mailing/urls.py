from django.urls import path
from . import views

urlpatterns = [
    path('', views.mailing, name='mailing'),
]
