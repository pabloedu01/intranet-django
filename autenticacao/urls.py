from django.urls import path
from . import views

urlpatterns = [
    path('autenticacao/login',views.login_simple,name='login'),
    path('autenticacao/logout',views.logout_view,name='logout'),
    path('autenticacao/login_simple',views.login_simple,name='login_simple')
]
