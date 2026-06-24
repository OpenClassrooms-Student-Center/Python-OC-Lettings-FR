"""
Admin registration module for lettings app
"""
from django.contrib import admin

from lettings.models import Address, Letting


admin.site.register(Letting)
admin.site.register(Address)
