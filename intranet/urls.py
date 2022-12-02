
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include, reverse_lazy
# from financeiro.views import *
# from rest_framework import routers
# from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from django.views.generic.base import RedirectView
from . import views

# router = routers.DefaultRouter()
# router.register(r'bancos', BancoViewSet)
# router.register(r'cargos', CargoViewSet)
# router.register(r'grupos', GrupoViewSet)
# router.register(r'empresas', EmpresaViewSet)
# router.register(r'beneficiarios', BeneficiarioViewSet)
admin.site.site_header = 'TUNAP do Brasil'
urlpatterns = [
    # path('api', include(router.urls)),
    # path('', views.indexPage,name='index'),
    path('admin/', admin.site.urls),
    path('auth/',include('autenticacao.urls')),
    # path('/',include('core.urls')),
    path('', RedirectView.as_view(url=reverse_lazy('admin:index'))),
    # path('admin/', admin.site.urls),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/api-auth/', include('rest_framework.urls')),
    url(r'^chaining/', include('smart_selects.urls'))
]
