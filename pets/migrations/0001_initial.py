# Generated by Django 4.1.6 on 2023-02-12 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("groups", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Pet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("age", models.IntegerField()),
                ("weight", models.FloatField()),
                (
                    "sex",
                    models.CharField(
                        choices=[
                            ("Male", "Male"),
                            ("Female", "Female"),
                            ("Not Informed", "Not Informed"),
                        ],
                        default="Not Informed",
                        max_length=20,
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="pets",
                        to="groups.group",
                    ),
                ),
            ],
        ),
    ]
