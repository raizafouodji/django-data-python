"""projetpython URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from HATVP_app.views import  Bootstrap3
from django.conf.urls import url

urlpatterns = [
    # pour qu'au lancement de django on n'atterisse sur l'application HATVP_app 
    path('',include('HATVP_app.urls')),
    path('admin/', admin.site.urls),
    url(r'^bootstrap3/$', Bootstrap3.as_view(), name="bootstrap"),
]
