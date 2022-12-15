from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/authentication/login')
def rel_comissao(request):
    context={"breadcrumb":{"parent":"Relatórios","child":"Comissão"}}
    # context={"breadcrumb":{"parent":"parent","child":"child"}}
    return render(request,'comissao.html',context)

def mapa_vendas(request):
    context={"breadcrumb":{"parent":"parent","child":"child"}}
    return render(request,'mapa_vendas.html',context)