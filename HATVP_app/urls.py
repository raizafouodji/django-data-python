from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import GeneralInformationListView


urlpatterns = [
    # definir la route pour la page home

   path('',views.index,name="index"),
    #path('',GeneralInformationListView.as_view(),name="index"),

    # definir la route vers result

    path('generic',views.generic,name="generic"),

    path('element',views.element,name="element")

]

urlpatterns += staticfiles_urlpatterns()