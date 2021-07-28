from django.urls import path
from .views import IndexView, SobreView, ContatoView

urlpatterns = [
    #path ('endereço/', MinhaView.as_view(), name='nome da url'),
    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('contato/', ContatoView.as_view(), name='contato'),
]