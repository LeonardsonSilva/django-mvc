from django.db import models
from .pessoa import Pessoa


class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=11, null=True, blank=True)

    class Meta:
        verbose_name = 'Pessoa Física'
        verbose_name_plural = 'Pessoas Físicas'
