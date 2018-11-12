# Generated by Django 2.1.3 on 2018-11-12 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0013_auto_20181112_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programa',
            name='categoria',
            field=models.IntegerField(choices=[(1, 'Esporte'), (2, 'Musica'), (3, 'Política'), (4, 'Cultura')], verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='programa',
            name='radio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='radio.Radio', verbose_name='Rádio'),
            preserve_default=False,
        ),
    ]
