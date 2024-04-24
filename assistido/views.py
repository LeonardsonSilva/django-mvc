from django.http.request import HttpRequest
from django.shortcuts import render

from . import models


def listar_assistidos(request: HttpRequest):
    assistidos = models.Assistido.objects.all()

    return render(
        request=request,
        template_name="assistido/lista_assistidos.html",
        context={
            "assistidos": assistidos,
        }
    )
