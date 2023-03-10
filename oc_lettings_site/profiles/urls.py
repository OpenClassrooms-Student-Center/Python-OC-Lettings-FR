from django.urls import path

from oc_lettings_site.profiles import views

app_name = 'profiles'

urlpatterns = [
    path('profiles/', views.index, name='index'),
    path('profiles/<str:username>/', views.profile, name='profile'),
]
