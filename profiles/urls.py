from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='profiles'),
    path('<str:username>/', views.profile, name='profile'),
]
