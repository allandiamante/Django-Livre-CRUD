"""Progressao URL Configuration

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

from django.urls import path
from .views import CampoCreate, AtividadeCreate, ClasseCreate, CampusCreate, StatusCreate
from .views import CampoUpdate, AtividadeUpdate
from .views import CampoDelete, AtividadeDelete
from .views import CampoList, AtividadeList
urlpatterns = [

    #path ('endereço/', MinhaView.as_view(), name='nome da url'),
    path('cadastrar/campo/', CampoCreate.as_view(), name='cadastrar-campo'),
    path('cadastrar/status/', StatusCreate.as_view(), name='cadastrar-status'),
    path('cadastrar/classe/', ClasseCreate.as_view(), name='cadastrar-classe'),
    path('cadastrar/campus/', CampusCreate.as_view(), name='cadastrar-campus'),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name='cadastrar-atividade'),

    #path('editar/campo/<var:pk>',)
    path('editar/campo/<int:pk>', CampoUpdate.as_view(), name='editar-campo'),
    path('editar/atividade/<int:pk>', AtividadeUpdate.as_view(), name='editar-atividade'),

    #path('excluir/campo/<var:pk>',)
    path('excluir/campo/<int:pk>', CampoDelete.as_view(), name='excluir-campo'),
    path('excluir/atividade/<int:pk>', AtividadeDelete.as_view(), name='excluir-atividade'),


    #path('listar/campo/',)
    path('listar/campos/', CampoList.as_view(), name='listar-campos'),
    path('listar/atividades/', AtividadeList.as_view(), name='listar-atividades'),

]
