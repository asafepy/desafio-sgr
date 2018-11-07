from rest_framework import serializers
from .models.radio import Radio
from .models.programa import Programa
from .models.programacao import Programacao


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
    # programa = ProgramaSerializer(read_only=True, many=True)
    

    get_programas = serializers.SerializerMethodField()

    def get_programas(self, obj):
        return obj.get_programas()


    class Meta:
        model = Programacao
        fields = ('url', 'nome','radio', 'get_programas',)