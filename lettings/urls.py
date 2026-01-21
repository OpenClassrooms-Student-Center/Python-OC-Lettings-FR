from django.urls import path
from . import views

app_name = 'lettings'  # namespace declaration

urlpatterns = [
    path('', views.index, name='index'),  # old lettings_index
    path('<int:letting_id>/', views.letting, name='letting'),
]
