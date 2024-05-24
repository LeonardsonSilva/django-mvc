from django.contrib import admin

from . import models


@admin.register(models.PessoaFisica)
class PessoaFisicaAdmin(admin.ModelAdmin):
    pass
