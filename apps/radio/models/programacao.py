from django.db import models
from apps.radio.models import Radio
from apps.radio.models import Programa
    
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

    def get_programas(self):
        id_programas = []
        print(self.programa.all())
        for i in self.programa.all():
            id_programas.append(i.id)
        print(id_programas)

        programas = Programa.objects.filter(id__in=id_programas)
        print(programas)
        return {}
