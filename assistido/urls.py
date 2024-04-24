from django.urls import path

from . import views

urlpatterns = [
    path(route='', view=views.listar_assistidos, name='listar_assistidos'),
]
