from django.db import models
from .related import RelatedInformation

class Field(RelatedInformation):
    __source__ = "HATVP_app/data/9_secteurs_activites.csv"

    name = models.CharField(max_length=64, verbose_name="secteur_activite")

    def __str__(self):
        return self.name
