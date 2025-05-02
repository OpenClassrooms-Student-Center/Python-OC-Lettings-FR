from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('oc_lettings_site', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                    name='Profile',
                ),
            ],
            database_operations=[
                migrations.AlterModelTable(
                    name='Profile',
                    table='profiles_profile',
                ),
            ],
        )
    ]