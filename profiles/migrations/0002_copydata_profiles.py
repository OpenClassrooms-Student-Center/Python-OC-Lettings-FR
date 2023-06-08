import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
        ("oc_lettings_site", "0003_auto_20230315_0705"),
    ]

    operations = [
        migrations.RunSQL("""
        insert into profiles_profile (
        id, user_id, favorite_city
        ) select 
        id, user_id, favorite_city 
        from oc_lettings_site_profile;
        """,
                          reverse_sql="""
                          insert into oc_lettings_site_profile (
                          id, user_id, favorite_city
                          ) select 
                          id, user_id, favorite_city 
                          from profiles_profile;
                          """)
            ]
