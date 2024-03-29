# Generated by Django 4.1.6 on 2023-02-13 01:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("traits", "0007_remove_trait_pets"),
        ("pets", "0004_remove_pet_traits"),
    ]

    operations = [
        migrations.AddField(
            model_name="pet",
            name="trait",
            field=models.ManyToManyField(related_name="pets", to="traits.trait"),
        ),
    ]
