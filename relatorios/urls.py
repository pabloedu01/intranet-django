from django.urls import path
from . import views

urlpatterns = [
    path('relatorios/comissao',views.rel_comissao,name='comissao'),
    path('relatorios/mapa_vendas',views.mapa_vendas,name='mapa_vendas'),
]