from django.contrib import admin
from apps.radio.models import Radio, Programa, Programacao

admin.site.register(Radio)
admin.site.register(Programa)
admin.site.register(Programacao)