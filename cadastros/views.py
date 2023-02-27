from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import *

# Create your views here.
@login_required(login_url="/login")
def beneficiarios_view(request):
    if request.GET.get('search'):
        beneficiarios_list = Beneficiario.objects.filter(name__icontains=request.GET.get('search'))
        pagina = request.GET.get('page')
        print(pagina)
    else: 
        beneficiarios_list = Beneficiario.objects.all()
    paginator = Paginator(beneficiarios_list, 1) # 10 itens por página
    page = request.GET.get('page')
    # Processa a pesquisa se houver uma string de busca
    
    try:
        beneficiarios = paginator.page(page)
    except PageNotAnInteger:
        beneficiarios = paginator.page(1)
    except EmptyPage:
        beneficiarios = paginator.page(paginator.num_pages)
    # Determina quais páginas serão exibidas na seção de paginação
    num_pages = paginator.num_pages
    current_page = beneficiarios.number
    if num_pages <= 5:
        page_range = range(1, num_pages + 1)
    elif current_page <= 3:
        page_range = range(1, 6)
    elif current_page >= num_pages - 2:
        page_range = range(num_pages - 4, num_pages + 1)
    else:
        page_range = range(current_page - 2, current_page + 3)

    context={"breadcrumb":{"parent":"Clientes","child":"Cadastros de clientes"},
             "beneficiarios":beneficiarios
             }

    return render(request,'list_beneficiarios/list_beneficiarios.html',context)