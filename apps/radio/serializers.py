from rest_framework import serializers
from .models.radio import Radio
from .models.programa import Programa
from .models.programacao import GradeProgramacao


class RadioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Radio
        fields = ('url', 'nome',)


class ProgramaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programa
        fields = ('url', 'nome',)


class GradeProgramacaoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = GradeProgramacao
        fields = ('url', 'nome','radio',)