import logging
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

logger = logging.getLogger(__name__)


def contact(request):
    success = False
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            full_message = (
                f"Nouveau message de {name} ({email}) :\n\n{message}"
            )

            try:
                send_mail(
                    subject=f"[Holiday Homes] {subject}",
                    message=full_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
                logger.info("Email de contact envoyé par %s", email)
                success = True
                form = ContactForm()
            except Exception as e:
                logger.error("Erreur envoi email : %s", e)
                form.add_error(None, "Une erreur est survenue. Veuillez réessayer.")

    return render(request, "contact/contact.html", {
        "form": form,
        "success": success,
    })
