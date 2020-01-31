from django.db import models
from .related import AutoModel
from .activity import Activity

class Domain(AutoModel):
    __source__ = "HATVP_app/data/7_domaines_intervention.csv"

    name = models.CharField(max_length=64, verbose_name="domaines_intervention_actions_menees")
    activity = models.ForeignKey(Activity, verbose_name="activite_id", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
