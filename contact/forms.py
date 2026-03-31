from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Votre nom",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Jean Dupont",
        }),
    )
    email = forms.EmailField(
        label="Votre email",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "jean@exemple.fr",
        }),
    )
    subject = forms.CharField(
        max_length=200,
        label="Sujet",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Question sur une location...",
        }),
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 5,
            "placeholder": "Votre message...",
        }),
    )
