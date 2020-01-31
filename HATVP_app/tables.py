from django_tables2_column_shifter.tables import ColumnShiftTableBootstrap2
from .models import *

# By default you probably inherit from django_table2.Table
# Change inherit to ColumnShiftTableBootstrap2
class GeneralInformationTable(ColumnShiftTableBootstrap2):

    column_default_show = ['id', 'name', 'category', 'address']
    order_by=None

    class Meta:
        model = GeneralInformation
        attrs = {'class': 'table table-bordered table-striped table-condensed'}

class ActionTable(ColumnShiftTableBootstrap2):

    column_default_show = ['desc', 'representant', 'more']
    order_by=None

    class Meta:
        model = Action
        attrs = {'class': 'table table-bordered table-striped table-condensed'}

class BeneficiaryTable(ColumnShiftTableBootstrap2):

    column_default_show = ['name', 'representant', 'own']
    order_by=None

    class Meta:
        model = Beneficiary
        attrs = {'class': 'table table-bordered table-striped table-condensed'}

class DecisionTable(ColumnShiftTableBootstrap2):

    column_default_show = ['name', 'representant']
    order_by=None

    class Meta:
        model = Decision
        attrs = {'class': 'table table-bordered table-striped table-condensed'}

class PeriodTable(ColumnShiftTableBootstrap2):

    column_default_show = ['publication', 'turnover', 'amount','no_turnover', 'nb_employees', 'incomplete_declaration']
    order_by=None

    class Meta:
        model = Period
        attrs = {'class': 'table table-bordered table-striped table-condensed'}

class ActivityTable(ColumnShiftTableBootstrap2):

    column_default_show = ['date', 'ref', 'desc']
    order_by=None

    class Meta:
        model = Activity
        attrs = {'class': 'table table-bordered table-striped table-condensed'}

class DirectorTable(ColumnShiftTableBootstrap2):

    order_by=None

    class Meta:
        model = Director
        attrs = {'class': 'table table-bordered table-striped table-condensed'}

class AssociateTable(ColumnShiftTableBootstrap2):

    order_by=None

    class Meta:
        model = Associate
        attrs = {'class': 'table table-bordered table-striped table-condensed'}

class ClientTable(ColumnShiftTableBootstrap2):

    order_by=None

    class Meta:
        model = Client
        attrs = {'class': 'table table-bordered table-striped table-condensed'}