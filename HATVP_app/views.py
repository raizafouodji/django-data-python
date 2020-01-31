from django.shortcuts import render
from django.http import HttpResponse
from HATVP_app.models import *
from django.db.models import Q
from pprint import pprint
from django_tables2 import SingleTableView
from django.views.generic import ListView
from HATVP_app.tables import *
from django.views.generic import TemplateView
from django_tables2.config import RequestConfig

# Create your views here.

def index(request):
    # afficher la page d'accueil 
    context = {}

    # variable dynamique definit dans la home et qui se charge a l'affichage de la page
    if request.GET :
        
        general_information_table_class = GeneralInformationTable
        actions_table_class = ActionTable
        beneficirary_table_class = BeneficiaryTable
        decision_table_class = DecisionTable
        period_table_class = PeriodTable
        activity_table_class = ActivityTable
        director_table_class = DirectorTable
        associate_table_class = AssociateTable
        client_table_class = ClientTable


        context['container_css'] = "col-xs-10 col-xs-offset-1"

        # query db
        #query = str('STORENGY')
        query = str(request.GET['q'])
        result = enterprise_details(query)
        

        # Build tabels
        gi_table = general_information_table_class(result['gi'])
        actions_table = actions_table_class(result['action'])
        beneficirary_table = beneficirary_table_class(result['beneficirary'])
        decision_table = decision_table_class(result['decision'])
        period_table = period_table_class(result['period'])
        activity_table = activity_table_class(result['activity'])
        director_table = director_table_class(result['director'])
        associate_table = associate_table_class(result['associate'])
        client_table = client_table_class(result['client'])
        # Turn on sorting and pagination
        RequestConfig(request, paginate={'per_page': 3}).configure(gi_table)
        RequestConfig(request, paginate={'per_page': 3}).configure(actions_table)
        RequestConfig(request, paginate={'per_page': 3}).configure(beneficirary_table)
        RequestConfig(request, paginate={'per_page': 3}).configure(decision_table)
        RequestConfig(request, paginate={'per_page': 3}).configure(period_table)
        RequestConfig(request, paginate={'per_page': 3}).configure(activity_table)
        RequestConfig(request, paginate={'per_page': 3}).configure(director_table)
        RequestConfig(request, paginate={'per_page': 3}).configure(associate_table)
        RequestConfig(request, paginate={'per_page': 3}).configure(client_table)

        context['gi'] = gi_table
        context['action'] = actions_table
        context['beneficirary'] = beneficirary_table
        context['decision'] = decision_table
        context['period'] = period_table
        context['activity'] = activity_table
        context['director'] = director_table
        context['associate'] = associate_table
        context['client'] = activity_table
        context['query'] = query

    return render(request,"testproject/test_bootstrap3.html",context=context)


def generic(request):
    # afficher la page d'accueil 

    # variable dynamique definit dans la home et qui se charge a l'affichage de la page
    query = str('STORENGY')
    details = enterprise_details(query)
    context['gi'] = details

    return render(request,"generic.html")


def element(request):
    # afficher la page d'accueil 

    # variable dynamique definit dans la home et qui se charge a l'affichage de la page

    return render(request,"elements.html")
def enterprise_details(query=None) :
    ids = []
    result={}
    result['gi'] = GeneralInformation.objects.filter(
        Q(name__icontains=query)
    ).distinct()
    print(result)
    ## collect ids
    for r in result['gi'] :
        print("{} | {} | {}".format(r.id,r.address,r.name))
        ids.append(r.id)

    result['action'] = Action.objects.filter(representant__in=ids)
    result['beneficirary'] = Beneficiary.objects.filter(representant__in=ids)
    result['decision'] = Decision.objects.filter(representant__in=ids)
    result['period'] = Period.objects.filter(representant__in=ids)
    result['director'] = Director.objects.filter(representant__in=ids)
    result['associate'] = Associate.objects.filter(representant__in=ids)
    result['client'] = Client.objects.filter(representant__in=ids)
    
    period_ids = []
    for r in result['period'] :
        print("{} | {} | {}".format(r.id,r.representant,r.publication))
        period_ids.append(r.id)

    result['activity'] = Activity.objects.filter(period__in=period_ids)
    return result


class GeneralInformationListView(ListView):
    model= GeneralInformation

class Bootstrap3(TemplateView):
    template_name = "testproject/test_bootstrap3.html"
    general_information_table_class = GeneralInformationTable
    actions_table_class = ActionTable
    beneficirary_table_class = BeneficiaryTable
    decision_table_class = DecisionTable
    period_table_class = PeriodTable
    activity_table_class = ActivityTable
    director_table_class = DirectorTable
    associate_table_class = AssociateTable
    client_table_class = ClientTable
    

    def get_context_data(self, **kwargs):
        context = super(Bootstrap3, self).get_context_data(**kwargs)
        context['container_css'] = "col-xs-10 col-xs-offset-1"

        # query db
        query = str('STORENGY')
        result = enterprise_details(query)
        

        # Build tabels
        gi_table = self.general_information_table_class(result['gi'])
        actions_table = self.actions_table_class(result['action'])
        beneficirary_table = self.beneficirary_table_class(result['beneficirary'])
        decision_table = self.decision_table_class(result['decision'])
        period_table = self.period_table_class(result['period'])
        activity_table = self.activity_table_class(result['activity'])
        director_table = self.director_table_class(result['director'])
        associate_table = self.associate_table_class(result['associate'])
        client_table = self.client_table_class(result['client'])
        # Turn on sorting and pagination
        RequestConfig(self.request, paginate={'per_page': 3}).configure(gi_table)
        RequestConfig(self.request, paginate={'per_page': 3}).configure(actions_table)
        RequestConfig(self.request, paginate={'per_page': 3}).configure(beneficirary_table)
        RequestConfig(self.request, paginate={'per_page': 3}).configure(decision_table)
        RequestConfig(self.request, paginate={'per_page': 3}).configure(period_table)
        RequestConfig(self.request, paginate={'per_page': 3}).configure(activity_table)
        RequestConfig(self.request, paginate={'per_page': 3}).configure(director_table)
        RequestConfig(self.request, paginate={'per_page': 3}).configure(associate_table)
        RequestConfig(self.request, paginate={'per_page': 3}).configure(client_table)

        context['gi'] = gi_table
        context['action'] = actions_table
        context['beneficirary'] = beneficirary_table
        context['decision'] = decision_table
        context['period'] = period_table
        context['activity'] = activity_table
        context['director'] = director_table
        context['associate'] = associate_table
        context['client'] = activity_table
        
        return context



