from django.urls import path
from . import views

urlpatterns = [

    # dashboard paths

    path('', views.indexPage,name='indexPage'),
    path('dashboard_default', views.dashboard_default,name='index')
]