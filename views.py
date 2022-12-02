import sys
sys.path.append(".")
import django_filters.rest_framework
from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import *
# from .serializers import *
# from rest_framework.permissions import IsAuthenticated
# from .pagination import CustomPageNumberPagination
# from django_filters.rest_framework import DjangoFilterBackend



# class BancoViewSet(viewsets.ModelViewSet):
#     # permission_classes = (IsAuthenticated,)
#     pagination_class = CustomPageNumberPagination
#     queryset = Banco.objects.all()
#     serializer_class = BancoSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['name']

# class CargoViewSet(viewsets.ModelViewSet):
#     # permission_classes = (IsAuthenticated,)
#     pagination_class = CustomPageNumberPagination
#     queryset = Cargo.objects.all()
#     serializer_class = CargoSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['name']

# class GrupoViewSet(viewsets.ModelViewSet):
#     # permission_classes = (IsAuthenticated,)
#     pagination_class = CustomPageNumberPagination
#     queryset = Grupo.objects.all()
#     qtd_clientes = Grupo.objects.all()
#     serializer_class = GrupoSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['name']

# class EmpresaViewSet(viewsets.ModelViewSet):
#     # permission_classes = (IsAuthenticated,)
#     pagination_class = CustomPageNumberPagination
#     queryset = Empresa.objects.all()
#     qtd_clientes = Empresa.objects.all()
#     serializer_class = EmpresaSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['name']

# class BeneficiarioViewSet(viewsets.ModelViewSet):
#     # permission_classes = (IsAuthenticated,)
#     pagination_class = CustomPageNumberPagination
#     queryset = Beneficiario.objects.all()
#     serializer_class = GrupoSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['nome']

