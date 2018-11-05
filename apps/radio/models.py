from django.db import models

class Radio(models.Model):
    
    nome = models.CharField("Rádio", max_length=100)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = 'Rádio'
        verbose_name_plural = 'Rádios'