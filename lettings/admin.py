from django.contrib import admin
from django.utils.html import format_html
from lettings.models import Address, Letting, LettingImage


class LettingImageInline(admin.TabularInline):
    model = LettingImage
    extra = 3
    max_num = 9  # + 1 image principale = 10 max
    fields = ("image", "order", "image_preview")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            # On utilise une f-string sur plusieurs lignes ou on coupe la chaîne
            return format_html(
                '<img src="{}" width="100" height="70" '
                'style="object-fit:cover;border-radius:4px"/>',
                obj.image.url
            )
        return "—"
    image_preview.short_description = "Aperçu"


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("number", "street", "city", "state", "zip_code", "country_iso_code")


@admin.register(Letting)
class LettingAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "get_address",
        "price_per_night",
        "rooms",
        "area",
        "image_preview")
    list_filter = ("address__city", "rooms")
    search_fields = ("title", "address__city", "address__street")
    inlines = [LettingImageInline]

    def get_address(self, obj):
        return str(obj.address)
    get_address.short_description = "Adresse"

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="80" height="60" '
                'style="object-fit:cover;border-radius:4px"/>',
                obj.image.url
            )
        return "—"
    image_preview.short_description = "Photo principale"
