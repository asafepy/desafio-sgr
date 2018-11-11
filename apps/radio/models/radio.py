from django.db import models
from django.db.models import Q
import datetime

NOW = datetime.datetime.now().strftime('%H:%M')

class Radio(models.Model):
    
    nome = models.CharField("Rádio", max_length=100)

    def __str__(self):
        return self.nome
        
    class Meta:
        verbose_name = 'Rádio'
        verbose_name_plural = 'Rádios'

    def programas(self):
        from apps.radio.models.programa import Programa
        return Programa.objects.filter(radio=self.pk).values("id", "nome")


    def make_url(self):
        return '/api/programa-atual/',self.pk,'/'

    def programa_atual(self):
        from apps.radio.models.programacao import GradeProgramacao
        grade_programacao = GradeProgramacao.objects.filter(Q(horario_inicio__lte=NOW) & 
                                                            Q(horario_fim__gte=NOW) & 
                                                            Q(grade__radio=self.pk))
        print(grade_programacao)
        for item in grade_programacao:
            print(item.programa.categoria)
            if item.programa.categoria == 1:
                return {'programa': item.programa.nome}
            return {'programa':item.programa.nome}
       
        return {}