from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/authentication/login')
def home(request):
    context={"breadcrumb":{"parent":"Relatórios","child":"Comissão"}}
    # context={"breadcrumb":{"parent":"parent","child":"child"}}
    return render(request,'home/index.html',context)