from django.contrib import admin
from django.urls import include, path

from oc_lettings_site import views as core_view

urlpatterns = [
    path("", core_view.index, name="index"),
    path("lettings/", include("lettings.urls", namespace="lettings")),
    path("profiles/", include("profiles.urls", namespace="profiles")),
    path("admin/", admin.site.urls),
]
