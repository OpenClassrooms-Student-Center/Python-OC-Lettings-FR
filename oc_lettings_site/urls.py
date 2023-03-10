from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('oc_lettings_site.home_site.urls')),
    path('', include('oc_lettings_site.lettings.urls')),
    path('', include('oc_lettings_site.profiles.urls')),
    path('admin/', admin.site.urls),
]
