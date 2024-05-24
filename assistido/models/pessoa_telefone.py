from django.db import models

from contrib.models import Telefone

from .pessoa import Pessoa


class PessoaTelefone(models.Model):
    pessoa = models.ForeignKey(to=Pessoa, null=False, blank=False, on_delete=models.PROTECT)
    telefone = models.ForeignKey(to=Telefone, null=False, blank=False, on_delete=models.PROTECT)

    class Meta:
        db_table = 'assistido_pessoa_telefone'
        verbose_name = 'Pessoa/Telefone'
        verbose_name_plural = 'Pessoas/Telefones'

    def __str__(self):
        return f'{str(self.pessoa)}/{str(self.telefone)}'
