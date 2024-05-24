from django.contrib import admin

from contrib import models


@admin.register(models.Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Telefone)
class TelefoneAdmin(admin.ModelAdmin):
    pass



