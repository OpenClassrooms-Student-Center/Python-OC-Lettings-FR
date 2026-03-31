from django.db import migrations, models


def generate_references(apps, schema_editor):
    Letting = apps.get_model('lettings', 'Letting')
    for letting in Letting.objects.all():
        letting.reference = f"LOC-{letting.pk:04d}"
        letting.save()


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0004_lettingimage'),  # adapte si nécessaire
    ]

    operations = [
        migrations.AddField(
            model_name='letting',
            name='reference',
            field=models.CharField(
                blank=True,
                default='',
                help_text='Référence unique du logement (ex: LOC-2026-001)',
                max_length=20,
            ),
        ),
        migrations.RunPython(generate_references),
        migrations.AlterField(
            model_name='letting',
            name='reference',
            field=models.CharField(
                blank=True,
                unique=True,
                help_text='Référence unique du logement (ex: LOC-2026-001)',
                max_length=20,
            ),
        ),
    ]
