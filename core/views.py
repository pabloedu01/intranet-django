from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http.response import HttpResponseRedirect
from .models import *
# from .forms import *

# Create your views here.



@login_required(login_url="/login")
def indexPage(request):
    return redirect('/dashboard_default')


def login_simple(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.GET:
                nextPage = request.GET['next']
                return HttpResponseRedirect(nextPage)
            else:
                return redirect('dashboard_ecommerce')
    else:
        form =AuthenticationForm()
    context={"breadcrumb":{"parent":"parent","child":"child"},"form":form}
    return render(request,'others/authentication/login/login.html',context)


def logout_view(request):
    logout(request)
    return redirect('/')

@login_required(login_url="/login")
def dashboard_default(request):
    context={"breadcrumb":{"parent":"Dashboard","child":"Default"}}
    return render(request,'general/dashboard/default/index.html',context)

