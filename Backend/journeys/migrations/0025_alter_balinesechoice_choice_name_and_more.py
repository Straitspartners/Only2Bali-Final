# Generated by Django 5.1.4 on 2024-12-28 07:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("journeys", "0024_alter_staytype_stay_type_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="balinesechoice",
            name="choice_name",
            field=models.CharField(
                choices=[
                    ("jimbaran_seafood", "Jimbaran Seafood"),
                    ("balinese_culinary", "Balinese Culinary"),
                    ("indonesian_food", "Indonesian Food"),
                    ("local_snacks", "Local Snacks"),
                    ("souvenir_foods", "Souvenir Foods"),
                ],
                max_length=50,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="dietarychoice",
            name="choice_name",
            field=models.CharField(
                choices=[("vegan", "Vegan"), ("keto", "Keto"), ("halal", "Halal")],
                max_length=50,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="nonvegetarianchoice",
            name="choice_name",
            field=models.CharField(
                choices=[
                    ("north_indian", "North Indian Non-Vegetarian"),
                    ("south_indian", "South Indian Non-Vegetarian"),
                ],
                max_length=50,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="vegetarianchoice",
            name="choice_name",
            field=models.CharField(
                choices=[
                    ("north_indian", "North Indian Vegetarian"),
                    ("south_indian", "South Indian Vegetarian"),
                    ("gujarati", "Gujarati Vegetarian"),
                    ("jain", "Jain Vegetarian"),
                ],
                max_length=50,
                unique=True,
            ),
        ),
    ]
