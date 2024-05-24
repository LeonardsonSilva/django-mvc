from django.db import models

from agendamento.models import GrupoAgendamento

from .defensoria import Defensoria

class DefensoriaGrupoAgendamento(models.Model):
    defensoria = models.ForeignKey(to=Defensoria, null=False, blank=False, on_delete=models.PROTECT)
    grupo_agendamento = models.ForeignKey(to=Defensoria, null=False, blank=False, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
