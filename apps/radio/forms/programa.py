from django import forms
from apps.radio.models.radio import Radio
from apps.radio.models.programa import Programa
from apps.radio.models.programacao import GradeProgramacao, Grade


class GradeProgramacaoForm(forms.ModelForm):
    


    # def __init__(self, *args, **kwargs):
        # super(GradeProgramacaoForm, self).__init__(*args, **kwargs)
        # self.fields['programa'].queryset = Programa.objects.filter(company=self.instance.programa.radio)

    class Meta:
        model = GradeProgramacao

        fields = ('__all__')