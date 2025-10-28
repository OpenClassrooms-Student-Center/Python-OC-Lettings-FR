"""
URL configuration for the 'lettings' application.

Defines the routes for the lettings index and individual letting detail pages.
"""
from django.urls import path

from . import views

app_name = 'lettings'
urlpatterns = [
    # Route for the lettings index page (e.g., /lettings/)
    path('', views.index, name='index'),
    # Route for a specific letting detail page (e.g., /lettings/1/)
    path('<int:letting_id>/', views.letting, name='letting'),
]