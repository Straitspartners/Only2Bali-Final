# Generated by Django 5.1.4 on 2024-12-14 06:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("journeys", "0010_alter_placestovisit_journey_preferences_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="placestovisit",
            name="journey_preferences",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="journeys.journeypreferences",
            ),
        ),
    ]
