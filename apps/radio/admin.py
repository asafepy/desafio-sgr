from django.contrib import admin
from apps.radio.models import Radio, Programa, Programacao

class ProgramacaoAdmin(admin.ModelAdmin):
    # regular stuff
    # def has_add_permission(self, request):
    #     return False

    class Media:
        js = (
            'assets/js/formset_handlers.js',   # app static folder
        )



admin.site.register(Radio)
admin.site.register(Programa)
admin.site.register(Programacao, ProgramacaoAdmin)