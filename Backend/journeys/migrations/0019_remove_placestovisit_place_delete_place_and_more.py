# Generated by Django 5.1.4 on 2024-12-27 06:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("journeys", "0018_rename_places_placestovisit_place"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="placestovisit",
            name="place",
        ),
        migrations.DeleteModel(
            name="Place",
        ),
        migrations.AddField(
            model_name="placestovisit",
            name="place",
            field=models.TextField(
                blank=True,
                choices=[
                    ("natural_beauty", "Natural Beauty and Beaches"),
                    ("local_culture", "Local Cultures and Traditions"),
                    ("wellness_relaxation", "Wellness and Relaxation"),
                    ("wedding_pre_wedding", "Wedding and Pre-Wedding"),
                    ("adventures_activities", "Adventures and Activities"),
                    ("local_culinary", "Local Culinary"),
                    ("shopping", "Shopping in Bali"),
                    ("luxury_experiences", "Luxury and Unique Experiences"),
                    ("others", "Others"),
                ],
                null=True,
            ),
        ),
    ]
