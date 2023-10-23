from django.db import migrations
from tools.tools import read_sql


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            read_sql('profiles', 'insert_data_from_oc.sql'),
            reverse_sql=read_sql('profiles', 'reverse_insert_data_from_oc.sql'),
        ),
    ]
