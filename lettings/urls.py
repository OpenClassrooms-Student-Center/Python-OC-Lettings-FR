"""
Module for the URL configuration of the lettings application.

This module maps URL patterns to their corresponding view functions.
"""

from django.urls import path
from . import views

app_name = 'lettings'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]
