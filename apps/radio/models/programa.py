from django.db import models

class Programa(models.Model):
    CATEGORIA_CHOICES = (
        (1, "Futebol"),
        (2, "Musica"),
        (3, "Política"),
        (4, "Cultura")
    )

    nome = models.CharField("Nome do programa", max_length=100)
    categoria = models.CharField('Categoria', choices=CATEGORIA_CHOICES, max_length=50)
    horario_exibicao = models.TimeField("Horário de exibição", auto_now=False, auto_now_add=False, )

    def __str__(self):
        return self.nome
        
    class Meta:
        ordering = ('categoria', 'horario_exibicao')

        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'