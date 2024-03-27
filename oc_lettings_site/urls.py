from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('lettings/',include('lettings.urls',namespace='lettings')),
    path('profiles/',include('profiles.urls',namespace='profiles')),
]
