from rest_framework import serializers
from .models.radio import Radio
from .models.programa import Programa
from .models.programacao import GradeProgramacao, Grade

class ProgramaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programa
        fields = ('id', 'url', 'nome', 'categoria')


        
class RadioSerializer(serializers.HyperlinkedModelSerializer):
    
    programas = serializers.SerializerMethodField()

    class Meta:
        model = Radio
        fields = ('url', 'nome', 'programas')
    
    def programas(self, obj):
        return obj.programas()



class GradeProgramacaoSerializer(serializers.HyperlinkedModelSerializer):
    
    grade = serializers.SerializerMethodField()
    
    class Meta:
        model = Grade
        fields = ('id', 'data_exibicao', 'radio', 'grade',)
    
    def grade(self, obj):
        return obj.grade()


class ProgramaAtualSerializer(serializers.HyperlinkedModelSerializer):
    
    programa_atual = serializers.SerializerMethodField()

    class Meta:
        model = Radio
        fields = ('id', 'nome', 'programa_atual',)
    
    def programa_atual(self, obj):
        return obj.programa_atual()