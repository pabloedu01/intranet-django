from django.db import models
from django.contrib.auth.models import User
# from smart_selects.db_fields import ChainedForeignKey
from cadastros.models import *

class Solicitacao_Pagamento(models.Model):
    beneficiario = models.ForeignKey(Beneficiario, related_name='beneficiario',on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=30, decimal_places=2, default=0, verbose_name='Valor')
    # value = models.MoneyField(max_digits=30, decimal_places=2, default=0, verbose_name='Valor')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Responsável')
    tipo_pagamento = models.ForeignKey(Tipo_Pagamento, on_delete=models.PROTECT, null=True, blank=True)
    status = models.ForeignKey(Status_Solicitacao, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        verbose_name = 'Solicitações de pgto'
    def __str__(self):
        if self.value is None:
            return ''
        else:     
            return str(self.value)