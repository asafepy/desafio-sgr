from django.db import models
from apps.radio.models import Radio
from apps.radio.models import Programa
    
class Grade(models.Model):
    
    data_exibicao = models.DateField("Data de exibição", auto_now=False, auto_now_add=False, )
    

class GradeProgramacao(models.Model):
    
    horario_exibicao = models.TimeField("Horário de exibição", auto_now=False, auto_now_add=False)
    grade = models.ForeignKey(Grade, verbose_name="Grade de Programação", on_delete=models.CASCADE)
    radio = models.ForeignKey(Radio, verbose_name="Rádio", on_delete=models.CASCADE)
    programa = models.ForeignKey(Programa, related_name='programas', verbose_name="Programa", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Programação'
        verbose_name_plural = 'Programações'

    def get_programas(self):
        programas = self.programa.all().filter()
        print()
        return {}
