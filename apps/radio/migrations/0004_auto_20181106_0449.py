# Generated by Django 2.1.3 on 2018-11-06 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0003_programa_programacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programacao',
            name='prgrama',
        ),
        migrations.AddField(
            model_name='programacao',
            name='prgrama',
            field=models.ManyToManyField(to='radio.Programa', verbose_name='Programa'),
        ),
    ]
