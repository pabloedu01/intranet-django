from django.urls import path
from . import views

urlpatterns = [
    path('authentication/login',views.login_simple,name='login'),
    path('authentication/logout',views.logout_view,name='logout'),
    path('authentication/login_simple',views.login_simple,name='login_simple')
]