from django.contrib import admin
from django.urls import path

from lettings import views as letttingsViews
from profiles import views as profilesViews

urlpatterns = [
    path('', letttingsViews.index, name='index'),
    path('lettings/', letttingsViews.lettings_index, name='lettings_index'),
    path('lettings/<int:letting_id>/', letttingsViews.letting, name='letting'),
    path('profiles/', profilesViews.profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', profilesViews.profile, name='profile'),
    path('admin/', admin.site.urls),
]
