from django.db import migrations


def new_tables(apps, schema_editor):
    old_profile_table = apps.get_model('oc_lettings_site', 'Profile')
    new_profile_table = apps.get_model('profiles', 'NewProfile')

    old_address_datas = old_profile_table.objects.all()

    for data in old_address_datas:
        new_letting_data = new_profile_table(id=data.id, favorite_city=data.favorite_city, user_id=data.user_id)
        new_letting_data.save()


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20240326_1424'),
    ]

    operations = [
        migrations.RunPython(new_tables),
    ]
