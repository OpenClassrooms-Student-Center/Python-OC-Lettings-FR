import os
from django.db import migrations
from oc_lettings_site import settings

def read_sql(filename):
    filepath = os.path.join(settings.BASE_DIR, 'lettings', 'sql', filename)
    with open(filepath, 'rb') as f:
        s = f.read()
    return s


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            read_sql('insert_data_from_oc.sql'),
            reverse_sql=read_sql('reverse_insert_data_from_oc.sql'),
        ),
    ]
