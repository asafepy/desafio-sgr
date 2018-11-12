from django.contrib import admin
from apps.radio.models import Radio, Programa, GradeProgramacao, Grade
from apps.radio.forms import GradeProgramacaoForm
from django.forms import ModelForm

class ProgramaInline(admin.TabularInline):
    model = Programa
    extra = 1

class RadioAdmin(admin.ModelAdmin):
    inlines = [
        ProgramaInline,
    ]

class GradeProgramacaoInline(admin.TabularInline):
    form = GradeProgramacaoForm
    model = GradeProgramacao
    extra = 1

class GradeAdmin(admin.ModelAdmin):
    inlines = [
        GradeProgramacaoInline,
    ]

    class Media:
        js = ('assets/js/formset_handlers.js',)  

admin.site.register(Radio, RadioAdmin)
admin.site.register(Grade, GradeAdmin)