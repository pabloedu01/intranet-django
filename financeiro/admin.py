from django.contrib import admin
from .models import *
from django.utils.html import format_html

@admin.register(Solicitacao_Pagamento)
class Solicitacao_PagamentoAdmin(admin.ModelAdmin):
    def empresa(self, obj):
        empresa = Empresa.objects.get(id=obj.beneficiario.empresa_id).name
        return(empresa)
    def grupo(self, obj):
        grupo = Grupo.objects.get(id=obj.beneficiario.grupo_id).name
        return(grupo)
    def deletar(self, obj):
        return format_html('<a class="btn" href="/admin/financeiro/solicitacao_pagamento/{}/delete/">deletar</a>', obj.id)
    def visualizar(self, obj):
        return format_html('<a class="btn" href="/admin/financeiro/solicitacao_pagamento/{}/change/">visualizar</a>', obj.id)
    autocomplete_fields = ['beneficiario']
    list_display = ['id','beneficiario','empresa','value','owner','status','tipo_pagamento','visualizar','deletar']
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

    def get_queryset(self, request):
        if request.user.is_superuser == False:
            queryset = super().get_queryset(request)
            queryset = queryset.filter(owner=request.user).all()
            return queryset
        else:
            queryset = super().get_queryset(request)
            queryset = queryset.all()
            return queryset