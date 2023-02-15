from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.
@admin.register(Banco)
class BancoAdmin(admin.ModelAdmin):
    list_display_links = ()
    search_fields = ['name']
    ordering = ['name']
    list_display = ('id_banco','name', 'numero_banco', 'Criação', 'Alteração')
    list_editable = ('name','numero_banco')
    list_filter = ('name',)
    def Criação(self, obj):
        data = obj.created_at
        data = data.strftime("%d/%m/%Y %H:%M:%S")
        return data
    def Alteração(self, obj):
        data = obj.updated_at
        data = data.strftime("%d/%m/%Y %H:%M:%S")
        return data
@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ['name']
    def Criação(self, obj):
        data = obj.created_at
        data = data.strftime("%d/%m/%Y %H:%M:%S")
        return data
    def Alteração(self, obj):
        data = obj.updated_at
        data = data.strftime("%d/%m/%Y %H:%M:%S")
        return data
    list_display = ('name', 'Criação', 'Alteração')

class TelefonesInline(admin.TabularInline):
    model = BeneficiarioTelefone
    extra = 0
    list_editable = ('telefone',)

class EmailInline(admin.TabularInline):
    model = BeneficiarioEmail
    extra = 0
    list_editable = ('email',)

class PixInline(admin.TabularInline):
    model = Pix
    extra = 0
    list_editable = ('chave_pix',)

class PixAdmin(admin.ModelAdmin):
    def Criação(self, obj):
        data = obj.created_at
        data = data.strftime("%d/%m/%Y %H:%M:%S")
        return data
    def Alteração(self, obj):
        data = obj.updated_at
        data = data.strftime("%d/%m/%Y %H:%M:%S")
        return data
    search_fields = ['chave_pix']
    list_display = ['chave_pix','Criação','Alteração']

class Conta_BancariaInline(admin.TabularInline):
    model = Conta_Bancaria
    extra = 0
    list_editable = ('banco','agencia','conta')
    
class Empresas_BancariaInline(admin.TabularInline):
    model = Empresa
    extra = 0

class CartaoInline(admin.TabularInline):
    model = Cartao
    extra = 0
    list_editable = ('banco','agencia','conta')
    readonly_fields = ('status',)
    list_display = ('numero_cartao')

@admin.register(Beneficiario)
class BeneficiarioAdmin(admin.ModelAdmin):
    
    def clean(self):
        cleaned_data = self.cleaned_data
        cpf = cleaned_data.get('cpf')
        cnpj = cleaned_data.get('cnpj')
        if cpf == cnpj:
            raise forms.ValidationError(u"You haven't set a valid department. Do you want to continue?")
        return cleaned_data
    autocomplete_fields = ['empresa']
    
    inlines = [TelefonesInline, EmailInline, PixInline, Conta_BancariaInline,CartaoInline]
    def Cargo(self, obj):
        return obj.cargo
    def Empresa(self, obj):
        return obj.empresa.name
    def Grupo(self, obj):
        return obj.empresa.grupo.name
    def Grupo(self, obj):
        return obj
    def Criação(self, obj):
        data = obj.created_at
        data = data.strftime("%d/%m/%Y %H:%M:%S")
        return data
    def Alteração(self, obj):
        data = obj.updated_at
        data = data.strftime("%d/%m/%Y %H:%M:%S")
        return data
    search_fields = ['name', 'cpf', 'cnpj']
    ordering = ['name']
    # raw_id_fields = ['empresa']
    def deletar(self, obj):
        return format_html('<a class="btn" href="/admin/cadastros/beneficiario/{}/delete/">deletar</a>', obj.id)
    def visualizar(self, obj):
        return format_html('<a class="btn" href="/admin/cadastros/beneficiario/{}/change/">visualizar</a>', obj.id)
    list_display = ('name','cpf', 'Cargo','Empresa',  'Criação', 'Alteração','visualizar','deletar')

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    search_fields = ['name']
    def grupo(self, obj):
        grupo = obj.id.name
        return grupo
    list_display = ['name']
    readonly_fields = ['name']

@admin.register(Grupo)
class GrupoaAdmin(admin.ModelAdmin):
    search_fields = ['name']
    inlines = [Empresas_BancariaInline]
    def grupo(self, obj):
        grupo = obj.name
        return grupo
    def empresas(self, obj):
        result = obj.empresas.count()
        if result > 1:
            result = f'{result} Empresas'
        elif result == 0:
            result = "Nenhuma empresa cadastrada"
        else:
            result = "1 Empresa"
        return (result)
    list_display = ['grupo','created_at', 'updated_at','empresas']

@admin.register(Tipo_Pagamento)
class Tipo_PagamentoADmin(admin.ModelAdmin):
    pass

@admin.register(Status_Solicitacao)
class Statis_SolicitacaoAdmin(admin.ModelAdmin):
    pass

@admin.register(Tipo_Cartao)
class Tipo_CartaoAdmin(admin.ModelAdmin):
    pass

@admin.register(Cartao)
class Tipo_Cartao(admin.ModelAdmin):
    # def ben(self, obj):
    #     ben = obj.id_beneficiario
    #     # Grupo.objects.get(id=obj.beneficiario.grupo_id).name
    #     print(ben)
    #     return(ben)
    search_fields = ['numero_cartao','id_beneficiario__name','tipo_cartao__tipo_cartao  ']
    list_display = ['numero_cartao','tipo_cartao','status','id_beneficiario']
    list_filter = ['status','tipo_cartao__tipo_cartao']
    # pass