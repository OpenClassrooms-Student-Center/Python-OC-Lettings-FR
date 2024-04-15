from django.contrib import admin
from .models import Profile  # Importez le modèle Profile de l'application profiles

admin.site.register(Profile)  # Enregistrez le modèle Profile dans l'interface d'administration
