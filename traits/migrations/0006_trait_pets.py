# Generated by Django 4.1.6 on 2023-02-13 00:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pets", "0004_remove_pet_traits"),
        ("traits", "0005_remove_trait_pets"),
    ]

    operations = [
        migrations.AddField(
            model_name="trait",
            name="pets",
            field=models.ManyToManyField(related_name="traits", to="pets.pet"),
        ),
    ]