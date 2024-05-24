from django.db import models

from agendamento.models import GrupoAgendamento

class Defensoria(models.Model):
    nome = models.CharField(max_length=120, null=False, blank=False)
    grupo_agendamento = models.ManyToManyField(to=GrupoAgendamento, through='DefensoriaGrupoAgedamento')

    def __str__(self):
        return self.nome
