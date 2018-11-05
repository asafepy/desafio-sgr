from django.db import models
from apps.radio.models import Radio

class Programa(models.Model):
    
    nome = models.CharField("Nome do programa", max_length=100)
    radio = models.ForeignKey(Radio, verbose_name="Rádio", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
        
    class Meta:
        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'