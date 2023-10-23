from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views


handler404 = 'oc_lettings_site.views.page_not_found'
handler500 = 'oc_lettings_site.views.server_error'


def trigger_error(request):
    division_by_zero = 1 / 0
    return division_by_zero


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
]


if settings.DEBUG:

    # This allows the error pages to be debugged during development.
    urlpatterns += [
        path(
            "404/",
            views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", views.server_error),
    ]
