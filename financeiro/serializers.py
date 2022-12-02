from rest_framework import routers, serializers, viewsets
from rest_framework.validators import UniqueForDateValidator
from .models import *

class BancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banco
        fields = ['id_banco','name','updated_at','created_at']

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ['id_cargo','name','updated_at','created_at']

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        # fields = ['name','updated_at','created_at']
        fields = '__all__'

class GrupoSerializer(serializers.ModelSerializer):
    empresas = EmpresaSerializer(many=True)
    class Meta:
        model = Grupo
        # fields = ['name','updated_at','created_at','empresas']
        fields = '__all__'
        # validators = [
        #     UniqueForDateValidator(
        #         queryset=Grupo.objects.all(),
        #         fields=['name']
        #     )
        # ]
        # exclude = ['id_grupo']
    def create(self, validated_data):
        empresas_data = validated_data.pop('empresas')
        grupo = Grupo.objects.create(**validated_data)
        for empresa_data in empresas_data:
            Empresa.objects.create(id_grupo=grupo, **empresa_data)
        return grupo

class BeneficiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiario
        fields = ['id','nome','updated_at','created_at', 'BeneficiarioTelefone']