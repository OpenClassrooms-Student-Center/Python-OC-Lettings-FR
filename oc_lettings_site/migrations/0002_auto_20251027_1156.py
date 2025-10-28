from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0001_initial'),
        # CRITICAL: Ensure data is copied (0002_data_migration) before deleting the source
        ('lettings', '0002_data_migration'), 
        ('profiles', '0002_data_migration'), 
    ]

    operations = [
        migrations.DeleteModel(
            name='Letting',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]