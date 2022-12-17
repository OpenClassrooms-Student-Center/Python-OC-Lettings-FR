from django.urls import path
from profiles import views as view_profile

app_name = 'profiles'
urlpatterns = [
    path('profiles/', view_profile.index, name='index'),
    path('profiles/<str:username>/', view_profile.profile, name='profile'),
]
