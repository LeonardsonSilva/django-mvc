from django.db import models

from contrib.models import Endereco

from .pessoa import Pessoa


class PessoaEndereco(models.Model):
    pessoa = models.ForeignKey(to=Pessoa, null=False, blank=False, on_delete=models.PROTECT)
    endereco = models.ForeignKey(to=Endereco, null=False, blank=False, on_delete=models.PROTECT)

    class Meta:
        db_table = 'assistido_pessoa_endereco'
        verbose_name = 'Pessoa/Endereço'
        verbose_name_plural = 'Pessoas/Endereços'

    def __str__(self):
        return f'{str(self.pessoa)}/{str(self.endereco)}'
