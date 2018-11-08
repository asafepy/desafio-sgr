from django.contrib import admin
from apps.radio.models import Radio, Programa, GradeProgramacao, Grade


class ProgramaInline(admin.TabularInline):
    model = Programa
    extra = 1

class RadioAdmin(admin.ModelAdmin):
    inlines = [
        ProgramaInline,
    ]

class GradeProgramacaoInline(admin.TabularInline):
    model = GradeProgramacao
    extra = 1
    
class GradeAdmin(admin.ModelAdmin):
    inlines = [
        GradeProgramacaoInline,
    ]


admin.site.register(Radio, RadioAdmin)
admin.site.register(Grade, GradeAdmin)