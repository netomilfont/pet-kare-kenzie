from django.db import models

class SexChoices(models.TextChoices):
    MALE = "Male"
    FEMALE = "Female"
    DEFAULT = "Not Informed"

class Pet(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(max_length=20, default=SexChoices.DEFAULT, choices=SexChoices.choices)

    group = models.ForeignKey(
        "groups.Group", 
        on_delete=models.PROTECT, 
        related_name="pets"
    )

    traits = models.ManyToManyField(
        "traits.Trait",
        related_name="pets"
    )

    def __repr__(self) -> str:
        return f'<Pet ({self.id}) -  {self.name}>'