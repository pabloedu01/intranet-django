from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPage,name='indexPage'),
    path('dashboard_default', views.dashboard_default,name='index'),
    # path('clientes', views.clientes_view,name='clientes'),
    path('login',views.login_simple,name='login'),
    path('logout_view',views.logout_view,name='logout_view'),
]