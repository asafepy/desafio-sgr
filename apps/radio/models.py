from django.db import models

class Radio(models.Model):
    
    nome = models.CharField("Rádio", max_length=100)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = 'Rádio'
        verbose_name_plural = 'Rádios'


class Programa(models.Model):
    
    nome = models.CharField("Nome do programa", max_length=100)
    radio = models.ForeignKey(Radio, verbose_name="Rádio", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
        
    class Meta:
        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'

        
class Programacao(models.Model):
    
    nome = models.CharField("Nome Programação", max_length=100)
    radio = models.ForeignKey(Radio, verbose_name="Rádio", on_delete=models.CASCADE)
    prgrama = models.ForeignKey(Programa, verbose_name="Programa", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Programação'
        verbose_name_plural = 'Programações'



