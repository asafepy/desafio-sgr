# Generated by Django 2.1.3 on 2018-11-05 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0002_auto_20181105_2033'),
        ('programa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='programa',
            name='radio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='radio.Radio', verbose_name='Rádio'),
            preserve_default=False,
        ),
    ]
