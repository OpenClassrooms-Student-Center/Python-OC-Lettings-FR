from django.db import migrations, models
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.CreateModel(
                    name="Profile",
                    fields=[
                        (
                            "id",
                            models.AutoField(
                                auto_created=True,
                                primary_key=True,
                                serialize=False,
                                verbose_name="ID",
                            ),
                        ),
                        (
                            "user",
                            models.OneToOneField(
                                on_delete=django.db.models.deletion.CASCADE,
                                related_name="new_user",
                                to=settings.AUTH_USER_MODEL,
                            ),
                        ),
                        (
                            "favorite_city",
                            models.CharField(max_length=64, blank=True),
                        ),
                    ],
                    options={
                        "db_table": "oc_lettings_site_profile",
                    },
                ),
            ],
        ),
    ]
