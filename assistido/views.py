from django.http.request import HttpRequest
from django.shortcuts import render
from django.http.response import JsonResponse

from . import forms
from . import models


def listar_assistidos(request: HttpRequest):
    assistidos = models.Pessoa.objects.none()
    form_filtro = forms.FiltroAssistido

    if request.method == 'GET':
        nome = request.GET.get('nome', '')

        form_filtro = forms.FiltroAssistido(request.GET or None)

        assistidos = models.Pessoa.objects.filter(
            nome__icontains=nome
        )

    return render(
        request=request,
        template_name="assistido/lista_assistidos.html",
        context={
            "assistidos": assistidos,
            "form_filtro": form_filtro,
        }
    )
