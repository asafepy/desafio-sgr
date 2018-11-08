from django.db import models
from apps.radio.models import Radio
from apps.radio.models import Programa
<<<<<<< HEAD
    
class Grade(models.Model):
=======
from django.db.models import Case, CharField, Value, When
from django.db.models import Avg, Count, Min, Sum

class Programacao(models.Model):
>>>>>>> abe7524404d415ffa9753401acd225f39b342db8
    
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
<<<<<<< HEAD
        programas = self.programa.all().filter()
        print()
=======
        
    #     Client.objects.annotate(
    #         rank=Case(
    #             When(programa__=Client.GOLD, then=Value('5%')),
    #             When(account_type=Client.PLATINUM, then=Value('10%')),
    #             default=Value('0%'),
    #             output_field=CharField(),
    #         ),
    #     ).values_list('name', 'discount')
    #     id_programas = []
    #     prioridade_futebol = []
    #     p = self.programa.all().order_by('categoria')
    #     print(p)

        # for item in self.programa.all():
        #     if item.categoria == 1:
        #     prioridade_futebol
        #     id_programas.append()
        # print(id_programas)

        # programas = Programa.objects.filter(id__in=id_programas)
        # print(programas)
>>>>>>> abe7524404d415ffa9753401acd225f39b342db8
        return {}
