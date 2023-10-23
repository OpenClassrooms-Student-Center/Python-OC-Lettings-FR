import os
from django.db import migrations
from tools.tools import read_sql

class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            read_sql('lettings', 'insert_data_from_oc.sql'),
            reverse_sql=read_sql('lettings', 'reverse_insert_data_from_oc.sql'),
        ),
    ]
