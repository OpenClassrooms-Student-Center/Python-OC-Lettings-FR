from django.urls import path
from . import views
# from lettings.views import Letting

app_name = 'lettings'

urlpatterns = [
    path('', views.index, name='index'),
    # Détails d'une location par son ID
    path('lettings/<int:letting_id>/', views.letting, name='letting'),

]
