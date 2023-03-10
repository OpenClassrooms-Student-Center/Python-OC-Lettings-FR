from django.urls import path

from oc_lettings_site.home_site import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
]
