from django.db import migrations

def copy_lettings_and_addresses(apps, schema_editor):
    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    NewAddress = apps.get_model('lettings', 'Address')
    NewLetting = apps.get_model('lettings', 'Letting')

    old_to_new_address = {}
    for old_addr in OldAddress.objects.all():
        new_addr = NewAddress.objects.create(
            number=old_addr.number,
            street=old_addr.street,
            city=old_addr.city,
            state=old_addr.state,
            zip_code=old_addr.zip_code,
            country_iso_code=old_addr.country_iso_code,
        )
        old_to_new_address[old_addr.id] = new_addr

    # Copier les lettings
    for old_letting in OldLetting.objects.all():
        NewLetting.objects.create(
            title=old_letting.title,
            address=old_to_new_address.get(old_letting.address_id)
        )

class Migration(migrations.Migration):
    dependencies = [
        ('lettings', '0001_initial'),
        ('oc_lettings_site', '__first__'),
    ]

    operations = [
        migrations.RunPython(copy_lettings_and_addresses),
    ] 