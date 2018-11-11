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


class GradeProgramacaoInlineForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(GradeProgramacaoInlineForm, self).__init__(*args, **kwargs)
        self.fields['radio'].queryset = Programa.objects.filter(
                                radio_id__exact=1)

    # for i in :
    # print(self.fields['radio'])

class GradeProgramacaoInline(admin.TabularInline):
    form = GradeProgramacaoForm
    model = GradeProgramacao
    extra = 1

    # def formfield_for_foreignkey(self, db_field, request=None, **kwargs):

    #     field = super(GradeProgramacaoInline, self).formfield_for_foreignkey(db_field, request, **kwargs)

    #     if db_field.name == 'inside_room':
    #         if request._obj_ is not None:
    #             field.queryset = field.queryset.filter(building__exact = request._obj_)  
    #         else:
    #             field.queryset = field.queryset.none()

    #     return field

class GradeAdmin(admin.ModelAdmin):
    # form = GradeProgramacaoInlineForm
    inlines = [
        GradeProgramacaoInline,
    ]
    # print(inlines)

    def get_formsets(self, request, obj=None):
        for inline in self.get_inline_instances(request):
            print(inline.get_formset(request, obj))

    # def formfield_for_foreignkey(self, db_field, request=None, **kwargs):

    #     field = super(GradeAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    #     # print(db_field.name)
    #     # if db_field.name == 'radio':
    #     #     if request._obj_ is not None:
    #     #         field.queryset = field.queryset.filter(building__exact = request._obj_)  
    #     #     else:
    #     #         field.queryset = field.queryset.none()

    #     return field

    class Media:
        js = ('assets/js/formset_handlers.js',)  

    


admin.site.register(Radio, RadioAdmin)
admin.site.register(Grade, GradeAdmin)