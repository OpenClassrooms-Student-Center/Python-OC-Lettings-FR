from django.db import migrations

def copy_profiles(apps, schema_editor):
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    NewProfile = apps.get_model('profiles', 'Profile')
    User = apps.get_model('auth', 'User')

    for old_profile in OldProfile.objects.all():
        NewProfile.objects.create(
            user=User.objects.get(pk=old_profile.user_id),
            favorite_city=old_profile.favorite_city,
        )

class Migration(migrations.Migration):
    dependencies = [
        ('profiles', '0001_initial'),
        ('oc_lettings_site', '__first__'),
    ]

    operations = [
        migrations.RunPython(copy_profiles),
    ] 