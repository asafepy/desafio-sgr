# Generated by Django 2.1.3 on 2018-11-08 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0009_merge_20181108_0302'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='programa',
            options={'ordering': ['categoria'], 'verbose_name': 'Programa', 'verbose_name_plural': 'Programas'},
        ),
        migrations.RemoveField(
            model_name='gradeprogramacao',
            name='radio',
        ),
        migrations.AddField(
            model_name='grade',
            name='radio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='radio.Radio', verbose_name='Rádio'),
            preserve_default=False,
        ),
    ]
