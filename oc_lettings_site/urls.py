from django.contrib import admin
from django.urls import include, path

from . import views


def trigger_issue(request):
    return 1 / 0


urlpatterns = [
    path('', views.index, name='index'),
    path('', include('profiles.urls')),
    path('', include('lettings.urls')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_issue),
]
