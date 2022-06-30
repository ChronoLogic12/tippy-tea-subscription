from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blogs, name='blog'),
    path('add/', views.add_blog, name='add_blog'),
]
