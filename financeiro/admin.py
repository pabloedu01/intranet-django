from datetime import datetime
from django.contrib import admin, messages
from .models import *
from django.utils.http import urlencode
from django.urls import reverse
from django.forms.widgets import Select
from django import forms
from django.core.exceptions import ValidationError


@admin.register(Solicitacao_Pagamento)
class Solicitacao_PagamentoAdmin(admin.ModelAdmin):
    def empresa(self, obj):
        empresa = Empresa.objects.get(id=obj.beneficiario.empresa_id).name
        return(empresa)
    def grupo(self, obj):
        grupo = Grupo.objects.get(id=obj.beneficiario.grupo_id).name
        return(grupo)
    raw_id_fields = ['beneficiario']
    list_display = ['id','beneficiario','grupo','empresa','value', 'status']
    list_filter = ['tipo_pagamento','owner']   
    
    def save_model(self, request, obj, form, change):
        if request.user.is_superuser == False:
            owner = request.user
            obj.owner = owner
        else:
            pass
        if request.user.is_superuser == False:
            obj.status = Status_Solicitacao.objects.get(id=1)
        super(Solicitacao_PagamentoAdmin, self).save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        if request.POST and request.POST.get('action') == 'delete_selected':
            if '2' in request.POST.getlist('_selected_action'):
                messages.info(request, f'Status não permite ser deletado!')
                return False
            return True
        return obj is None or obj.pk != 2

    def get_queryset(self, request):
        if request.user.is_superuser == False:
            queryset = super().get_queryset(request)
            queryset = queryset.filter(owner=request.user).all()
            return queryset
        else:
            queryset = super().get_queryset(request)
            queryset = queryset.all()
            return queryset