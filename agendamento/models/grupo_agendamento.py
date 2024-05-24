from django.db import models

from defensoria.models import Defensoria


class GrupoAgendamento(models.Model):
    nome = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        verbose_name = 'Grupo de Agendamento'
        verbose_name_plural = 'Grupos de Agendamentos'
