# Generated by Django 2.1.3 on 2018-11-10 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0011_auto_20181110_0140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gradeprogramacao',
            old_name='data_fim',
            new_name='horario_fim',
        ),
        migrations.RenameField(
            model_name='gradeprogramacao',
            old_name='data_inicio',
            new_name='horario_inicio',
        ),
    ]
