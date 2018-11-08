from django.db import models
from apps.radio.models.radio import Radio

class Programa(models.Model):
    
    CATEGORIA_CHOICES = (
        (1, "Futebol"),
        (2, "Musica"),
        (3, "Política"),
        (4, "Cultura")
    )

    nome = models.CharField("Nome do programa", max_length=100)
    categoria = models.IntegerField('Categoria', choices=CATEGORIA_CHOICES)
    radio = models.ForeignKey(Radio, verbose_name="Rádio", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
        
    class Meta:
        ordering = ['categoria']
        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'



