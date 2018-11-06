from rest_framework import serializers
from .models import Radio, Programa, Programacao


class RadioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Radio
        fields = ('url', 'nome',)


class ProgramaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programa
        fields = ('url', 'nome',)


class ProgramacaoSerializer(serializers.HyperlinkedModelSerializer):
    radio = RadioSerializer(read_only=True)
    programa = ProgramaSerializer(read_only=True, many=True)
    

    class Meta:
        model = Programacao
        fields = ('url', 'nome','radio', 'programa',)