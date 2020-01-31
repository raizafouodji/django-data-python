from django.contrib import admin
from django.contrib import admin
from .models import GeneralInformation, Period, Activity,Action,Decision,Domain,Target,Beneficiary
from .models import Observation, Affiliation, Director, Associate, Client, Level,Field
# register your model
admin.site.register(GeneralInformation)
admin.site.register(Affiliation)
admin.site.register(Director)
admin.site.register(Associate)
admin.site.register(Client)
admin.site.register(Level)
admin.site.register(Period)
admin.site.register(Activity)
admin.site.register(Action)
admin.site.register(Decision)
admin.site.register(Domain)
admin.site.register(Target)
admin.site.register(Observation)
admin.site.register(Field)
admin.site.register(Beneficiary)

