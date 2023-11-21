"""define lettings url"""
from django.urls import path

from . import views

APP_NAME = "lettings"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:letting_id>/", views.letting, name="letting"),
]
