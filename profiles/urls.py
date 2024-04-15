from django.urls import path
from . import views

urlpatterns = [
    # Liste des profils
    path('profiles/', views.profiles_index, name='index'),
    # Détails d'un profil par son nom d'utilisateur#
    path('profiles/<str:username>/', views.profile, name='profile'),
]
