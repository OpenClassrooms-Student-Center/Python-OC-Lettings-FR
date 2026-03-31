"""Models for the profiles application.

This module defines the tenant profile (dossier locataire)
linked to a Django User account.
"""

from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField


class Profile(models.Model):

    SITUATION_CHOICES = [
        ("employe", "Employé"),
        ("independant", "Indépendant / Auto-entrepreneur"),
        ("etudiant", "Étudiant"),
        ("retraite", "Retraité"),
        ("sans_emploi", "Sans emploi"),
        ("autre", "Autre"),
    ]

    STATUS_CHOICES = [
        ("en_attente", "En attente"),
        ("valide", "Validé"),
        ("refuse", "Refusé"),
    ]

    # Lien utilisateur
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Informations personnelles
    date_of_birth = models.DateField(
                                    null=True,
                                    blank=True,
                                    verbose_name="Date de naissance"
                                    )
    phone = models.CharField(max_length=20, blank=True, verbose_name="Téléphone")
    current_address = models.CharField(
                                        max_length=256,
                                        blank=True,
                                        verbose_name="Adresse actuelle"
                                        )

    # Situation professionnelle
    situation = models.CharField(
        max_length=20,
        choices=SITUATION_CHOICES,
        blank=True,
        verbose_name="Situation professionnelle"
    )
    employer_name = models.CharField(
                                    max_length=128,
                                    blank=True,
                                    verbose_name="Employeur / Établissement"
                                    )
    monthly_income = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Revenus mensuels nets (€)"
    )

    # Garant
    has_guarantor = models.BooleanField(default=False, verbose_name="A un garant")
    guarantor_name = models.CharField(
                                    max_length=128,
                                    blank=True,
                                    verbose_name="Nom du garant"
                                    )
    guarantor_income = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Revenus mensuels du garant (€)"
    )
    guarantor_on_smic = models.BooleanField(
        default=False,
        verbose_name="Garant au SMIC"
    )

    # Pièces justificatives
    id_document = CloudinaryField(
                        "CNI / Passeport",
                        blank=True,
                        null=True
                        )
    proof_of_address = CloudinaryField(
                        "Justificatif de domicile",
                        blank=True,
                        null=True
                        )
    payslip = CloudinaryField("Fiche de paie", blank=True, null=True)

    # Statut du dossier
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="en_attente",
        verbose_name="Statut du dossier"
    )
    admin_notes = models.TextField(
        blank=True,
        verbose_name="Notes de l'agence"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    desired_letting = models.ForeignKey(
        'lettings.Letting',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Logement souhaité",
        related_name="candidates"
    )

    def __str__(self):
        return self.user.username

    @property
    def is_smic(self):
        """Vérifie si les revenus sont proches du SMIC (1 767 € net en 2024)."""
        SMIC_NET = 1767
        if self.monthly_income:
            return self.monthly_income <= SMIC_NET
        return False

    @property
    def guarantor_is_smic(self):
        """Vérifie si le garant est au SMIC."""
        SMIC_NET = 1767
        if self.guarantor_income:
            return self.guarantor_income <= SMIC_NET
        return False
