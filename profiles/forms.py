from django import forms
from profiles.models import Profile
from lettings.models import Letting


class TenantProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        required=False, label="Prénom",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        required=False, label="Nom",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField(
        required=False, label="Email",
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    desired_letting = forms.ModelChoiceField(
        queryset=Letting.objects.all(),
        required=False,
        label="Logement souhaité",
        empty_label="-- Choisir un logement --",
        widget=forms.Select(attrs={"class": "form-select"})
    )

    class Meta:
        model = Profile
        fields = (
            "date_of_birth", "phone", "current_address",
            "situation", "employer_name", "monthly_income",
            "has_guarantor", "guarantor_name",
            "guarantor_income", "guarantor_on_smic",
            "id_document", "proof_of_address", "payslip",
            "desired_letting",
        )
        widgets = {
            "date_of_birth": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "current_address": forms.TextInput(attrs={"class": "form-control"}),
            "situation": forms.Select(attrs={"class": "form-select"}),
            "employer_name": forms.TextInput(attrs={"class": "form-control"}),
            "monthly_income": forms.NumberInput(attrs={"class": "form-control"}),
            "has_guarantor": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "guarantor_name": forms.TextInput(attrs={"class": "form-control"}),
            "guarantor_income": forms.NumberInput(attrs={"class": "form-control"}),
            "guarantor_on_smic": forms.CheckboxInput(
                attrs={"class": "form-check-input"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and hasattr(self.instance, "user"):
            self.fields["first_name"].initial = self.instance.user.first_name
            self.fields["last_name"].initial = self.instance.user.last_name
            self.fields["email"].initial = self.instance.user.email
        # Affiche référence + titre dans le dropdown
        self.fields["desired_letting"].queryset = Letting.objects.all()
        self.fields["desired_letting"].label_from_instance = lambda obj: (
            f"{obj.reference} — {obj.title}" if obj.reference else obj.title
        )

    def save(self, commit=True):
        profile = super().save(commit=False)
        user = profile.user
        user.first_name = self.cleaned_data.get("first_name", "")
        user.last_name = self.cleaned_data.get("last_name", "")
        user.email = self.cleaned_data.get("email", "")
        if commit:
            user.save()
            profile.save()
        return profile
