from django.shortcuts import render
from django.http import HttpResponse
from .utils import password_is_valid
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http.response import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate

def login_simple(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user:
            print('passou')
            login(request, user)
            return redirect('/')
        else:
            return redirect('/authentication/login')

    else:
        form =AuthenticationForm()
    context={"breadcrumb":{"parent":"parent","child":"child"},"form":form}
    return render(request,'authentication/login/login.html',context)


def logout_view(request):
    print('aqui')
    logout(request)
    return redirect('login')

def login_with_bg_image(request):
    context={"breadcrumb":{"parent":"parent","child":"child"}}
    return render(request,'others/authentication/login-one/login_one.html',context)

def login_with_image_two(request):
    context={"breadcrumb":{"parent":"parent","child":"child"}}
    return render(request,'others/authentication/login-two/login_two.html',context)

def login_with_validation(request):
    context={"breadcrumb":{"parent":"parent","child":"child"}}
    return render(request,'others/authentication/login-bs-validation/login-bs-validation.html',context)

def login_with_tooltip(request):
    context={"breadcrumb":{"parent":"parent","child":"child"}}
    return render(request,'others/authentication/login-bs-tt-validation/login-bs-tt-validation.html',context)

def login_with_sweetalert(request):
    context={"breadcrumb":{"parent":"parent","child":"child"}}
    return render(request,'others/authentication/login-sa-validation/login-sa-validation.html',context)

def register_simple(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('dashboard_ecommerce')
    else:
        form = UserCreationForm()
    
    return render(request,'others/authentication/sign-up/sign-up.html',{"form":form})

def register_with_bg_image(request):
    context={"breadcrumb":{"parent":"parent","child":"child"}}
    return render(request,'others/authentication/sign-up-one/sign-up-one.html',context)

def register_with_bg_video(request):
    context={"breadcrumb":{"parent":"parent","child":"child"}}
    return render(request,'others/authentication/sign-up-two/sign-up-two.html',context)


def unlock_user(request):
    context={"breadcrumb":{"parent":"parent","child":"child"}}
    return render(request,'others/authentication/unlock/unlock.html',context)


def forget_password(request):
    context={"breadcrumb":{"parent":"parent","child":"child"}}
    return render(request,'others/authentication/forget-password/forget-password.html',context)


def create_password(request):
    context={"breadcrumb":{"parent":"parent","child":"child"}}
    return render(request,'others/authentication/create-password/creat-password.html',context)


def maintenance(request):
    context={"breadcrumb":{"parent":"parent","child":"child"}}
    return render(request,'others/authentication/maintenance/maintenance.html',context)