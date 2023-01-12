from django.urls import path
from . import views

urlpatterns = [
    path('dashboards',views.home,name='home'),
]