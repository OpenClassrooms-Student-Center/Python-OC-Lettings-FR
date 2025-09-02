from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
    # Test URLs for error pages
    path('404/', views.test_404, name='test_404'),
    path('500/', views.test_500, name='test_500'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
