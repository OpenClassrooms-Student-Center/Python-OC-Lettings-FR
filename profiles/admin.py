from django.contrib import admin
from django.utils.html import format_html
from profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "get_full_name", "situation", "monthly_income",
        "has_guarantor", "guarantor_on_smic", "status_badge", "created_at"
    )
    list_filter = ("status", "situation", "has_guarantor", "guarantor_on_smic")
    search_fields = (
        "user__username", "user__first_name",
        "user__last_name", "user__email"
    )
    readonly_fields = (
        "created_at", "updated_at",
        "id_preview", "address_preview", "payslip_preview"
    )

    fieldsets = (
        ("Compte", {
            "fields": ("user",)
        }),
        ("Informations personnelles", {
            "fields": ("date_of_birth", "phone", "current_address")
        }),
        ("Situation professionnelle", {
            "fields": ("situation", "employer_name", "monthly_income")
        }),
        ("Garant", {
            "fields": (
                "has_guarantor", "guarantor_name",
                "guarantor_income", "guarantor_on_smic"
            )
        }),
        ("Pièces justificatives", {
            "fields": (
                "id_document", "id_preview",
                "proof_of_address", "address_preview",
                "payslip", "payslip_preview",
            )
        }),
        ("Dossier", {
            "fields": ("status", "admin_notes", "created_at", "updated_at")
        }),
    )

    def get_full_name(self, obj):
        full = f"{obj.user.first_name} {obj.user.last_name}".strip()
        return full if full else obj.user.username
    get_full_name.short_description = "Locataire"

    def status_badge(self, obj):
        colors = {
            "en_attente": "#f0ad4e",
            "valide": "#5cb85c",
            "refuse": "#d9534f",
        }
        labels = {
            "en_attente": "En attente",
            "valide": "Validé",
            "refuse": "Refusé",
        }
        color = colors.get(obj.status, "#aaa")
        label = labels.get(obj.status, obj.status)
        return format_html(
            '<span style="background:{};color:#fff;padding:3px 10px;'
            'border-radius:12px;font-size:12px;">{}</span>',
            color, label
        )
    status_badge.short_description = "Statut"

    def _doc_preview(self, field):
        if field:
            return format_html(
                '<a href="{}" target="_blank">'
                '<img src="{}" width="120" height="80" '
                'style="object-fit:cover;border-radius:4px;"/>'
                '</a>', field.url, field.url
            )
        return "—"

    def id_preview(self, obj):
        return self._doc_preview(obj.id_document)
    id_preview.short_description = "Aperçu CNI"

    def address_preview(self, obj):
        return self._doc_preview(obj.proof_of_address)
    address_preview.short_description = "Aperçu justificatif"

    def payslip_preview(self, obj):
        return self._doc_preview(obj.payslip)
    payslip_preview.short_description = "Aperçu fiche de paie"
