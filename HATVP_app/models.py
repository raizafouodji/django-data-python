from django.db import models

'''
class InformationsGenerales(models.Model):
    representants_id = models.IntegerField(primary_key=True)
    adresse = models.CharField(null=True,blank=True,max_length=200)
    code_postal = models.CharField(null=True,blank=True,max_length=200)
    derniere_publication_activite = models.DateTimeField(null=True,blank=True) #A CHANGER EN DATE models.DateTimeField(null=True,blank=True,null=True,blank=True)
    date_premiere_publication = models.DateTimeField(null=True,blank=True) #A CHANGER EN DATE
    declaration_organisation_appartenance = models.BooleanField(null=True,blank=True)
    declaration_tiers = models.BooleanField(null=True,blank=True)
    denomination = models.CharField(null=True,blank=True,max_length=200)
    identifiant_national = models.CharField(null=True,blank=True,max_length=200)
    activites_publiees =  models.BooleanField(null=True,blank=True)
    page_facebook =models.CharField(null=True,blank=True,max_length=200)
    page_linkedin=models.CharField(null=True,blank=True,max_length=200)
    page_twitter=models.CharField(null=True,blank=True,max_length=200)
    site_web=models.CharField(null=True,blank=True,max_length=200)
    nom_usage_HATVP=models.CharField(null=True,blank=True,max_length=200)
    pays=models.CharField(null=True,blank=True,max_length=200)
    sigle_HATVP=models.CharField(null=True,blank=True,max_length=200)
    type_identifiant_national=models.CharField(null=True,blank=True,max_length=200)
    ville=models.CharField(null=True,blank=True,max_length=200)
    label_categorie_organisation=models.CharField(null=True,blank=True,max_length=200)

    
class Dirigeants(models.Model):
    civilite_dirigeant=models.CharField(null=True,blank=True,max_length=200)
    fonction_dirigeant=models.CharField(null=True,blank=True,max_length=200)
    nom_dirigeant=models.CharField(null=True,blank=True,max_length=200)
    prenom_dirigeant=models.CharField(null=True,blank=True,max_length=200)
    representants_id = models.ForeignKey(Informations_generales,on_delete=models.CASCADE)
    nom_prenom_dirigeant=models.CharField(null=True,blank=True,max_length=200)


class Collaborateurs(models.Model):
    civilite_collaborateur=models.CharField(null=True,blank=True,max_length=200)
    fonction_collaborateur=models.CharField(null=True,blank=True,max_length=200)
    nom_collaborateur=models.CharField(null=True,blank=True,max_length=200)
    prenom_collaborateur=models.CharField(null=True,blank=True,max_length=200)
    representants_id = models.ForeignKey(Informations_generales,on_delete=models.CASCADE)
    nom_prenom_collaborateur=models.CharField(null=True,blank=True,max_length=200)

class Clients(models.Model):
    representants_id = models.ForeignKey(Informations_generales,on_delete=models.CASCADE)
    denomination_client=models.CharField(null=True,blank=True,max_length=200)
    identifiant_national_client=models.CharField(null=True,blank=True,max_length=200)
    type_identifiant_national_client=models.CharField(null=True,blank=True,max_length=200)
'''
class Actionmenee(models.Model):
    action = models.CharField(null = True,max_length = 144, verbose_name = 'action')
    action_id = models.IntegerField(primary_key = True , default = 0, verbose_name = 'action_id')
    action_autre = models.CharField(null = True, max_length = 144, verbose_name = 'action_autre')
    def __str__(self):
        return self.action


class Ministeres(models.Model):
    action_id = models.ForeignKey(Actionmenee,on_delete=models.CASCADE, default = 0, verbose_name = 'action_id')
    responsable_public = models.CharField(null = True, max_length = 150, verbose_name = 'responsable_public')
    departement_ministeriel = models.CharField(max_length = 150, verbose_name = 'departement_ministriel')
    def __str__(self):
        return self.departement_ministeriel



class Benificiares(models.Model):
    beneficiaire = models.CharField(max_length = 155, null = True, verbose_name = 'beneficiaire')
    action_id = models.ForeignKey(Actionmenee,on_delete=models.CASCADE, default = 0, verbose_name = 'action_id')
    en_propre = models.BooleanField(null = True, blank = True, verbose_name = 'en_propre')
    def __str__(self):
        return self.beneficiaire
    '''
class GeneralInformation(models.Model):
    id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=256, blank=True)
    zipcode = models.CharField(max_length=256, blank=True)
    last_activity = models.DateTimeField(blank=True, null=True)
    first_activity = models.DateTimeField(blank=True, null=True)
    organizations = models.BooleanField(default=False)
    third_parties = models.BooleanField(default=False)
    name = models.CharField(max_length=256)
    nif = models.CharField(max_length=256, unique=True)
    activities = models.BooleanField(default=False)
    facebook = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    website = models.URLField(blank=True)
    hatvp_name = models.CharField(max_length=256)
    country = models.CharField(max_length=32)
    acronym = models.CharField(max_length=32)
    nif_type = models.CharField(max_length=8)
    town = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
'''












    







"""    #table contenant les information general

class information_general(models.Model):
    representants_id = exercices_id = models.AutoField(primary_key=True)
    adresse = models.CharField()
    code_postal = models.IntegerField()
    derniere_publication_activite = models.DateTimeField()
    date_premiere_publication = models.DateTimeField()
    declaration_organisation_appartenance = models.BooleanField()
    declaration_tiers = models.BooleanField()
    denomination = models.CharField()
    identifiant_national = models.CharField()
    activites_publieespage_facebook = models.BooleanField()
    page_linkedin = models.CharField()
    page_twitter = models.CharField( blank =True)
    site_web = models.CharField(blank =True)
    nom_usage_HATVP = models.CharField(blank= True)
    pays  = models.CharField( blank = True)
    sigle_HATVP = models.CharField(blank = True )
    type_identifiant_national = models.CharField(blank =True)
    ville = models.CharField(blank =True)
    label_categorie_organisation = models.CharField(blank = True)
"""


