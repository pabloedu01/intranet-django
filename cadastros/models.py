from django.db import models
from django.core.exceptions import ValidationError

class Banco(models.Model):
    id_banco = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True, unique=True, verbose_name='name do banco')
    numero_banco = models.CharField(max_length=10, blank=True, null=True, unique=True, verbose_name='Número do banco')
    updated_at = models.DateTimeField(blank = True, auto_now=True, verbose_name='Data de atualização')
    created_at = models.DateTimeField(blank = True, auto_now_add=True, verbose_name='Data de criação')
    
    def __str__(self):
        if self.name is None:
            return ''
        else:     
            return self.name

class Cargo(models.Model):
    id_cargo = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(blank = True, auto_now_add=True)
    def __str__(self):
        if self.name is None:
            return ''
        else:     
            return self.name

class Grupo(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=240)
    updated_at = models.DateTimeField(blank = True, auto_now=True)
    created_at = models.DateTimeField(blank = True, auto_now_add=True)
    
    class Meta:
        unique_together = (('name',))
    def __str__(self):
        if self.name is None:
            return ''
        else:     
            return self.name

class Empresa(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=240, verbose_name='Razão Social')
    cnpj = models.CharField(max_length=14, blank=True)
    grupo = models.ForeignKey('Grupo',related_name='empresas', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(blank = True, auto_now=True)
    created_at = models.DateTimeField(blank = True, auto_now_add=True)
    class Meta:
        unique_together = ('cnpj',)
        db_table = 'empresas'
    def __str__(self):
        if self.name is None:
            return ''
        else:     
            return self.name

class BeneficiarioTelefone(models.Model):
    id = models.BigAutoField(primary_key=True)
    telefone = models.CharField(unique=True, max_length=100, blank=True)
    id_beneficiario = models.ForeignKey('Beneficiario', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    default = models.BooleanField(blank=True, null=True, verbose_name='Padrão', default=False)

    class Meta:
        unique_together = (('id_beneficiario', 'default'),)
    def __str__(self):
        if self.telefone is None:
            return ''
        else:     
            return self.telefone
    class Meta:
        verbose_name_plural = 'Telefones'

class BeneficiarioEmail(models.Model):
    id_Email = models.BigAutoField(primary_key=True)
    email = models.EmailField(unique=True, max_length=254, blank=True)
    id_beneficiario = models.ForeignKey('Beneficiario', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    default = models.BooleanField(blank=True, null=True, verbose_name='Padrão', default=False)

    class Meta:
        unique_together = (('id_beneficiario', 'default'),('email',))
    def __str__(self):
        if self.email is None:
            return ''
        else:     
            return self.email
    class Meta:
        verbose_name_plural = 'Emails'

class Beneficiario(models.Model):
    id = models.BigAutoField(primary_key=True)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    cnpj = models.CharField(unique=True, max_length=19, blank=True, null=True)
    cpf = models.CharField(unique=True, max_length=19, blank=True, null=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, default=1)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.name is None:
            return ''
        else:     
            return self.name
    def clean(self):
        if self.cnpj and self.cpf is not None:
            raise ValidationError([
                ValidationError('Escolha apenas CPF ou CNPJ', code='')
            ])
        else:
            pass

    def save(self, *args, **kwargs):
            self.full_clean()
            return super().save(*args, **kwargs)
        

class Pix(models.Model):
    id_pix = models.BigAutoField(primary_key=True)
    id_beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    chave_pix = models.CharField(max_length=240, blank=True, unique=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    default = models.BooleanField(blank=True, null=True, verbose_name='Padrão', default=False)

    class Meta:
        verbose_name_plural = 'Chaves Pix'
     
class Tipo_Pagamento(models.Model):
    id_tipo_pagamento = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=240)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        if self.nome is None:
            return ''
        else:     
            return self.nome
    class Meta:
        verbose_name_plural = 'Tipos de pagamento'
        unique_together = (('nome',))

class Conta_Bancaria(models.Model):
    tipos_de_contas = (
        ("C", "Corrente"),
        ("P", "Poupança")
    )
    id_cc = models.BigAutoField(primary_key=True)
    id_beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=240, choices=tipos_de_contas)
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
    agencia = models.CharField(max_length=240)
    conta = models.CharField(max_length=240)    
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    default = models.BooleanField(blank=True, null=True, verbose_name='Padrão', default=False)

    class Meta:
        verbose_name_plural = 'Contas Bancárias'

class Tipo_Cartao(models.Model):
    id_tipo_cartap = models.BigAutoField(primary_key=True)
    tipo_cartao = models.CharField(max_length=250, unique=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Tipos de cartões'
    def __str__(self):
        if self.tipo_cartao is None:
            return ''
        else:     
            return self.tipo_cartao

class Cartao(models.Model):
    status = (
        ("s", "Solicitado"),
        ("p", "Pendente"),
        ("a", "Ativo"),
        ("c", "Cancelado")
    )
    
    id_cartao = models.BigAutoField(primary_key=True)
    id_beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=240, choices=status, default="p")
    tipo_cartao = models.ForeignKey(Tipo_Cartao, on_delete=models.DO_NOTHING)
    default = models.BooleanField(blank=True, null=True, verbose_name='Padrão', default=False)
    numero_cartao = models.CharField(max_length=240, blank=True, null=True)
    endereco_entrega = models.CharField(max_length=240, blank=True)    
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # default = models.BooleanField(blank=True, null=True, verbose_name='Padrão', default=False)
        
    class Meta:
        verbose_name_plural = 'Cartões'
        unique_together = (('tipo_cartao','id_beneficiario'))
        unique_together = (('numero_cartao','tipo_cartao'))
    def __str__(self):
        if self.tipo_cartao.tipo_cartao is None:
            return ''
        else:     
            return self.tipo_cartao.tipo_cartao

class Status_Solicitacao(models.Model):
    name = models.CharField(max_length=255, unique=True)
    # readonly_fields = ['usuario','status']        
    def __str__(self):
        if self.name is None:
            return ''
        else:     
            return self.name