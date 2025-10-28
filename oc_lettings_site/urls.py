"""
The root URL configuration for the oc_lettings_site project.

Delegates URL patterns to the 'lettings' and 'profiles' applications. 
Also defines the custom handlers for 404 and 500 errors.
"""
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    # Main Index View (from oc_lettings_site/views.py)
    path('', views.index, name='index'),

    # Lettings App URLs (using include for modularity)
    path('lettings/', include('lettings.urls')),

    # Profiles App URLs (using include for modularity)
    path('profiles/', include('profiles.urls')),

    # Admin interface
    path('admin/', admin.site.urls),
]


# Custom Error Handlers
# These variables must be set at the root URLconf level to override Django's defaults.
handler404 = 'oc_lettings_site.views.custom_404_view'
handler500 = 'oc_lettings_site.views.custom_500_view'