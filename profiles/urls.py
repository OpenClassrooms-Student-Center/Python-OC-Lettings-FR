"""
URL configuration for the 'profiles' application.

Defines the routes for the profiles index and individual user profile detail pages.
"""
from django.urls import path

from . import views

app_name = 'profiles'
urlpatterns = [
    # Route for the profiles index page (e.g., /profiles/)
    path('', views.index, name='index'),
    # Route for a specific profile detail page (e.g., /profiles/johndoe/)
    path('<str:username>/', views.profile, name='profile'),
]