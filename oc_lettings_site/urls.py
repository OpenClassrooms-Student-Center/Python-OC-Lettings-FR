from django.contrib import admin
from django.urls import path
from home import views as home_views  # Importez la vue de l'application home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.index, name='index'),  # URL pour la page d'accueil
    # Autres URLs pour les applications incluses
]
