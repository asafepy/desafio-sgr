from django.db import models
from django.utils.translation import gettext as _

class Radio(models.Model):
    
    nome = models.CharField("Rádio", max_length=100)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = 'Rádio'
        verbose_name_plural = 'Rádios'


class Programa(models.Model):
    CATEGORIA_CHOICES = (
        ('futebol', _("Futebol")),
        ('musica', _("Musica")),
        ('politica', _("Política")),
        ('cultura', _("Cultura"))
    )

    nome = models.CharField("Nome do programa", max_length=100)
    categoria = models.CharField('Categoria', choices=CATEGORIA_CHOICES, max_length=50)
    horario_exibicao = models.TimeField("Horário de exibição", auto_now=False, auto_now_add=False, )

    def __str__(self):
        return self.nome
        
    class Meta:
        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'

        
class Programacao(models.Model):
    
    nome = models.CharField("Nome Programação", max_length=100)
    radio = models.ForeignKey(Radio, verbose_name="Rádio", on_delete=models.CASCADE)
    programa = models.ManyToManyField(Programa, related_name='programas', verbose_name="Programa")

    data_exibicao = models.DateField("Data de exibição", auto_now=False, auto_now_add=False, )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Programação'
        verbose_name_plural = 'Programações'



