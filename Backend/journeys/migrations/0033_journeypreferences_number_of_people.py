# Generated by Django 5.1.4 on 2025-02-17 07:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("journeys", "0032_alter_traveldetails_international_airport"),
    ]

    operations = [
        migrations.AddField(
            model_name="journeypreferences",
            name="number_of_people",
            field=models.IntegerField(default=1),
        ),
    ]
