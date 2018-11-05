from django.db import models
from apps.radio.models import Radio
from apps.programa.models import Programa

class Programacao(models.Model):
    
    nome = models.CharField("Nome Programação", max_length=100)
    radio = models.ForeignKey(Radio, verbose_name="Rádio", on_delete=models.CASCADE)
    prgrama = models.ForeignKey(Programa, verbose_name="Programa", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Programação'
        verbose_name_plural = 'Programações'