from argparse import Namespace
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('', include('profiles.urls'), namespace='profile'),
    path('', include('lettings.urls'), namespace='lettings'),
]
