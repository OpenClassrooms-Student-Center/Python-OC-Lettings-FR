from django.urls import path

from . import views

urlpatterns = [
    path("lettings/", views.index, name="index"),
    path("lettings/<int:letting_id>/", views.letting, name="letting"),
]
