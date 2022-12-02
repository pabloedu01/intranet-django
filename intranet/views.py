from django.shortcuts import render,redirect

def indexPage(request):
    context={"breadcrumb":{"parent":"Dashboard","child":"Default"}}
    return render(request,'index.html',context)