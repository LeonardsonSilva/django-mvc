from django.shortcuts import render
from django.http.request import HttpRequest


def index(request: HttpRequest):
    return render(
        request=request,
        template_name="assistido/lista_assistidos.html",
        context={}
    )
