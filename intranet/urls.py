
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
import os

admin.site.site_header = os.environ.get('DJANGO_NAME_PORTAL')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/admin')),
    path('', RedirectView.as_view(url='/authentication/login')),
    path('',include('authentication.urls')),
    path('',include('relatorios.urls')),
    path('',include('financeiro.urls')),
    path('',include('dashboards.urls')),
    path('__debug__/', include('debug_toolbar.urls')),

]