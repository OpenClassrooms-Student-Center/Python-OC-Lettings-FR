from django.contrib import admin

from lettings.models import Letting
from lettings.models import Address
from profiles.models import Profile

# Register the models in the admin site.
admin.site.register(Letting)
admin.site.register(Address)
admin.site.register(Profile)

# Fix pluralization of the Address model.
Address._meta.verbose_name_plural = "Adresses"
