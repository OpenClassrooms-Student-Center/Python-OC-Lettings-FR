from django.contrib import admin
from django.urls import path, include

from lettings import views as view_letting

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_letting.home, name='index'),
    path('', include('lettings.urls')),
    path('', include('profiles.urls')),

]
