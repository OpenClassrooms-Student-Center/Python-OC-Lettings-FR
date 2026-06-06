"""
URLs module for oc_lettings_site app.
Include the lettings and profiles apps urls
"""
from django.contrib import admin
from django.urls import path, include

from . import views

handler404 = "oc_lettings_site.views.custom_404"

handler500 = "oc_lettings_site.views.custom_500"
urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
]
