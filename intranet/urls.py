
from django.contrib import admin
# from django.conf.urls import url
from django.urls import path, include, reverse_lazy
from django.views.generic.base import RedirectView
from . import views

admin.site.site_header = 'TUNAP do Brasil'
urlpatterns = [
    path('', views.indexPage,name='indexPage'),
    path('',include('autenticacao.urls')),
    path('',include('dashboards.urls')),
    path('admin/', admin.site.urls),
    path('auth/',include('autenticacao.urls')),
]
