from django.db import migrations


def new_tables(apps, schema_editor):
    old_address_table = apps.get_model('oc_lettings_site', 'Address')
    new_address_table = apps.get_model('lettings', 'NewAddress')
    old_letting_table = apps.get_model('oc_lettings_site', 'Letting')
    new_letting_table = apps.get_model('lettings', 'NewLetting')

    old_address_datas = old_address_table.objects.all()
    old_letting_datas = old_letting_table.objects.all()

    for data in old_address_datas:
        new_letting_data = new_address_table(id=data.id, number=data.number, street=data.street, city=data.city, state=data.state, zip_code=data.zip_code, country_iso_code=data.country_iso_code)
        new_letting_data.save()

    for data in old_letting_datas:
        new_letting_data = new_letting_table(id=data.id, title=data.title, address_id=data.address_id)
        new_letting_data.save()

class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0002_auto_20240326_1424'),
    ]

    operations = [
        migrations.RunPython(new_tables),
    ]
