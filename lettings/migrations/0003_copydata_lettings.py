import django.core.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("lettings", "0002_auto_20230420_1047"),
        ("oc_lettings_site", "0003_auto_20230315_0705"),
                    ]

    operations = [
        migrations.RunSQL("""
        insert into lettings_address(
        id, number,street, city, state,zip_code, country_iso_code
        ) select id, number,street, city, state,zip_code, country_iso_code
         from oc_lettings_site_address;
        """,
                          reverse_sql="""
                          insert into oc_lettings_site_address(
                          id, number,street, city, state,zip_code, country_iso_code
                          ) select id, number,street, city, state,zip_code, country_iso_code
                           from lettings_address;
                          """),
        migrations.RunSQL("""
        insert into lettings_letting (
        id, title, address_id
        )
        select  id, title, address_id from oc_lettings_site_letting;
        """,
                          reverse_sql="""
                          insert into oc_lettings_site_letting (
                          id, title, address_id
                          )select id, title, address_id from lettings_letting;
                          """),
            ]
