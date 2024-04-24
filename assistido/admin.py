from django.contrib import admin

from . import models


@admin.register(models.Assistido)
class AssistidoAdmin(admin.ModelAdmin):
    pass

