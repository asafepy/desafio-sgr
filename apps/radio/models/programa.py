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
<<<<<<< HEAD
    radio = models.ForeignKey(Radio, verbose_name="Rádio", on_delete=models.CASCADE)
=======
    horario_exibicao = models.TimeField("Horário de exibição", auto_now=False, auto_now_add=False, )
>>>>>>> abe7524404d415ffa9753401acd225f39b342db8

    def __str__(self):
        return self.nome
        
    class Meta:
<<<<<<< HEAD
        ordering = ['categoria']
=======
        ordering = ['horario_exibicao']

>>>>>>> abe7524404d415ffa9753401acd225f39b342db8
        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'



