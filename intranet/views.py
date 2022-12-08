from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url="/autenticacao/login")
def indexPage(request):
    return redirect('/dashboard_default')