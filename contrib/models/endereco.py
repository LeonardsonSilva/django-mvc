from django.db import models

# Create your models here.

class Endereco(models.Model):

    logradouro = models.CharField(max_length=240, null=False, blank=False)

    def __str__(self):
        return self.logradouro
