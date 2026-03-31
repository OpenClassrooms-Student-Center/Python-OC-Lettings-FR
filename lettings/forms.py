from django import forms


class LettingFilterForm(forms.Form):
    city = forms.CharField(
        required=False,
        label="Ville",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Ex : Paris, Lyon...",
        }),
    )
    price_min = forms.DecimalField(
        required=False,
        label="Prix min (€/nuit)",
        min_value=0,
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "0",
        }),
    )
    price_max = forms.DecimalField(
        required=False,
        label="Prix max (€/nuit)",
        min_value=0,
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "500",
        }),
    )
    rooms_min = forms.IntegerField(
        required=False,
        label="Pièces minimum",
        min_value=1,
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "1",
        }),
    )
    area_min = forms.IntegerField(
        required=False,
        label="Surface min (m²)",
        min_value=0,
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "20",
        }),
    )
