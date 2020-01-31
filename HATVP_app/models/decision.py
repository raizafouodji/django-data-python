from django.db import models
from .related import AutoModel
from .information import GeneralInformation

class Decision(AutoModel):
    __source__ = "HATVP_app/data/12_decisions_concernees.csv"

    name = models.CharField(max_length=256, verbose_name="decision_concernee")
    representant = models.ForeignKey(GeneralInformation, verbose_name="action_representation_interet_id", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
