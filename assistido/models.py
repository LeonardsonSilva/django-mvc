from django.db import models


class Assistido(models.Model):
    nome = models.CharField(max_length=120)

    class Meta:
        verbose_name = 'assistido'
        verbose_name_plural = 'assistidos'

    def __str__(self):
        return self.nome

