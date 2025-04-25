"""
Module for the profiles URL configuration.
This module maps URL patterns to views for the profiles application.
"""

from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.profile, name='profile'),
]
