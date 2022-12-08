from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/login")
def indexPage(request):
    return redirect('/dashboard_default')

@login_required(login_url="/login")
def dashboard_default(request):
    context={"breadcrumb":{"parent":"Dashboard","child":"Default"}}
    return render(request,'dashboard/default/index.html',context)


# @login_required(login_url="/login")
# def dashboard_ecommerce(request):
#     context={"breadcrumb":{"parent":"Dashboard","child":"Ecommerce"}}
#     return render(request,'general/dashboard/ecommerce/dashboard-02.html',context)


# @login_required(login_url="/login")
# def dashboard_project(request):
#     context={"breadcrumb":{"parent":"Dashboard","child":"project-Dashboard"}}
#     return render(request,'general/dashboard/project/dashboard-03.html',context)

# @login_required(login_url="/login")
# def cadastrar_solicitacao(request):
#     context={"breadcrumb":{"parent":"Dashboard","child":"project-Dashboard"}}
#     return render(request,'solicitacao-pagamento/solicitacao-pagamento.html',context)
