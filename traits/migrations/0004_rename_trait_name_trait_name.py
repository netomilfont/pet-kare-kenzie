# Generated by Django 4.1.6 on 2023-02-13 00:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("traits", "0003_rename_name_trait_trait_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="trait",
            old_name="trait_name",
            new_name="name",
        ),
    ]