from django.db import models
from apps.radio.models import Radio
from apps.radio.models import Programa
from datetime import datetime

class Grade(models.Model):
    
    data_exibicao = models.DateField("Data de exibição", auto_now=False, auto_now_add=False, )
    radio = models.ForeignKey(Radio, verbose_name="Rádio", on_delete=models.CASCADE)

    def grade(self):
        return GradeProgramacao.objects.filter(grade_id=self.pk).values("horario_inicio", "horario_fim", "programa__nome")

    def __str__(self):
        return self.radio.nome

    class Meta:
        verbose_name = 'Grade de Programação'
        verbose_name_plural = 'Grades de Programações'

class GradeProgramacao(models.Model):
    
    horario_inicio = models.TimeField("Horário de Início", auto_now=False, auto_now_add=False, blank=True, null=True)
    horario_fim = models.TimeField("Horário de Fim", auto_now=False, auto_now_add=False, blank=True, null=True)
    grade = models.ForeignKey(Grade, verbose_name="Grade de Programação", related_name='grade_programacao',  on_delete=models.CASCADE)
    programa = models.ForeignKey(Programa, 
                                 related_name='programas', 
                                #  limit_choices_to={'radio_id': self.grade__radio}, 
                                 verbose_name="Programa", 
                                 on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'

    def get_programa_atual(self):
        programas = self.programa
        print(programas)
        return {}


