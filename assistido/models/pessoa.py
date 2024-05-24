from django.db import models

from contrib.models import Endereco, Telefone


class Pessoa(models.Model):
    nome = models.CharField(max_length=240)
    email = models.EmailField(max_length=120)
    telefones = models.ManyToManyField(to=Telefone, through='PessoaTelefone', through_fields=('pessoa', 'telefone'))
    enderecos = models.ManyToManyField(to=Endereco, through='PessoaEndereco', through_fields=('pessoa', 'endereco'))
