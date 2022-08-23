from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.index, name='home'),

    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
]
