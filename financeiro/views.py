from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.db.models import Avg, Sum, Count
from django.db.models.functions import Coalesce
from django.http.response import HttpResponseRedirect


@login_required(login_url='/authentication/login')
def solicitacao_pagamento(request):
    if request.method == "GET":
        try:
            busca = request.GET['busca']
        except:
            busca = ''

    if request.user.is_superuser == True:
        solicitacoes = Solicitacao_Pagamento.objects.filter(beneficiario__name__icontains=busca).select_related('beneficiario','beneficiario__empresa','beneficiario__empresa__grupo')
        tipo_pagamento = solicitacoes.filter(beneficiario__name__icontains=busca).values('tipo_pagamento__pk','tipo_pagamento__nome').annotate(count=Count('pk', distinct=True)).order_by()
        if solicitacoes:
            total = Solicitacao_Pagamento.objects.filter(beneficiario__name__icontains=busca).aggregate(total = Sum('value'))
        else:
            total = {"total":0}
    else:
        solicitacoes = Solicitacao_Pagamento.objects.filter(beneficiario__name__icontains=busca,owner=request.user.id).select_related('beneficiario','beneficiario__empresa','beneficiario__empresa__grupo')
        tipo_pagamento = solicitacoes.filter(beneficiario__name__icontains=busca,owner=request.user.id).values('tipo_pagamento__pk','tipo_pagamento__nome').annotate(count=Count('pk', distinct=True)).order_by()
        if solicitacoes:
            total = Solicitacao_Pagamento.objects.filter(beneficiario__name__icontains=busca,owner=request.user.id).aggregate(total = Sum('value'))
        else:
            total = {"total":0}
    for i in tipo_pagamento:
        # print(i)
        print(i['tipo_pagamento__nome'])
    paginator = Paginator(solicitacoes, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'solicitacao_pagamento.html', {
        "page_obj": page_obj,
        "busca":busca,
        "breadcrumb":{"parent":"Financeiro","child":"Solicitação de pagamento"},
        "total":total
        })

@login_required(login_url="/authentication/login")
def deletesolicitacao_pagamento(request, pk):
    item = Solicitacao_Pagamento.objects.get(id=pk)
    
    if request.method == "POST":
        item.delete()
        print('POST')
    else:
        print('get')
    return HttpResponseRedirect("/financeiro/solicitacao_pagamento")