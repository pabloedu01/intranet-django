
from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
import os

admin.site.site_header = os.environ.get('DJANGO_NAME_PORTAL')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/admin')),
]
