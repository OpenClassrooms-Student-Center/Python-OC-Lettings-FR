from django.urls import path
from lettings import views as view_letting

app_name = 'lettings'
urlpatterns = [

    path('lettings/', view_letting.index, name='index'),
    path('lettings/<int:letting_id>/', view_letting.letting, name='letting'),
]
