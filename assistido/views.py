from django.http.request import HttpRequest
from django.shortcuts import render
from django.http.response import JsonResponse

from . import forms
from . import models


def listar_assistidos(request: HttpRequest):
    assistidos = models.Assistido.objects.none()
    form_filtro = forms.FiltroAssistido

    if request.method == 'GET':
        nome = request.GET.get('nome', '')

        form_filtro = forms.FiltroAssistido(request.GET or None)

        assistidos = models.Assistido.objects.filter(
            nome__icontains=nome
        ).select_related(
            'endereco',
        )

        a = list(assistidos)

    return JsonResponse(list(assistidos), safe=False)
