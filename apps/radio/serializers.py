from rest_framework import serializers
from .models.radio import Radio
from .models.programa import Programa
from .models.programacao import GradeProgramacao, Grade


class RadioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Radio
        fields = ('url', 'nome',)


class ProgramaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programa
        fields = ('id', 'url', 'nome', 'categoria')


class GradeSerializer(serializers.HyperlinkedModelSerializer):

    get_programa_atual = serializers.SerializerMethodField()
    related_name = serializers.StringRelatedField(many=True)

    def get_programa_atual(self, obj):
        return obj.get_programa_atual()

    class Meta:
        model = Grade
        fields = ('url','data_exibicao', 'radio', 'related_name',)



