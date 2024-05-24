from django.db import models


class Telefone(models.Model):
    TIPO_CELULAR = 10
    TIPO_RESIDENCIAL = 20
    TIPO_COMERCIAL = 30
    TIPO_WHATSAPP = 40
    TIPO_SMS = 50

    LISTA_TIPOS = (
        (TIPO_CELULAR, 'Celular'),
        (TIPO_RESIDENCIAL, 'Residencial'),
        (TIPO_COMERCIAL, 'Comercial'),
        (TIPO_WHATSAPP, 'Whatsapp'),
        (TIPO_SMS, 'SMS'),
    )

    ddd = models.CharField(max_length=2, null=False, blank=False)
    numero = models.CharField(max_length=9, null=False, blank=False)
    tipo = models.SmallIntegerField(choices=LISTA_TIPOS, null=False, blank=False, default=TIPO_CELULAR)


    def __str__(self):
        return f'({self.ddd}) {self.numero}'
