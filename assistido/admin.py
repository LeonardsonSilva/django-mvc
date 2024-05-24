from django.contrib import admin

from . import models


@admin.register(models.PessoaFisica)
class PessoaFisicaAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PessoaEndereco)
class PessoaEnderecoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PessoaTelefone)
class PessoaTelefoneAdmin(admin.ModelAdmin):
    pass
