from django.contrib import admin
from .models import Letting  # Importez le modèle Letting de l'application lettings
from .models import Address


admin.site.register(Letting)  # Enregistrez le modèle Letting dans l'interface d'administration

admin.site.register(Address)
