from rest_framework import serializers
from .models.radio import Radio
from .models.programa import Programa
from .models.programacao import GradeProgramacao, Grade

class ProgramaSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Programa
        fields = ('id', 'url', 'nome',)

class RadioSerializer(serializers.ModelSerializer):
    
    programas = serializers.SerializerMethodField()
    
    class Meta:
        model = Radio
        fields = ('url', 'nome', 'programas')
    
    def programas(self, obj):
        return obj.programas()

class GradeSerializer(serializers.HyperlinkedModelSerializer):
    
    grade = serializers.SerializerMethodField()
    
    class Meta:
        model = Grade
        fields = ('id', 'url', 'data_exibicao', 'radio', 'grade',)
    
    def grade(self, obj):
        return obj.grade()

    def to_representation(self, instance):
        
        representation = super(GradeSerializer, self).to_representation(instance)
        representation['radio'] = instance.radio.nome

        return representation
    

class GradeListSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Grade
        fields = ('url', 'radio',)

    def to_representation(self, instance):
        
        representation = super(GradeListSerializer, self).to_representation(instance)
        representation['radio'] = instance.radio.nome

        return representation

class ProgramaAtualListSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Radio
        fields = ('nome', 'url',)

    def to_representation(self, instance):
        
        url = str(self.context['request'].build_absolute_uri()).strip()+str(instance.pk)+'/'
        
        representation = super(ProgramaAtualListSerializer, self).to_representation(instance)
        representation['url'] = url

        return representation


class ProgramaAtualSerializer(serializers.HyperlinkedModelSerializer):
    
    programa_atual = serializers.SerializerMethodField()
    
    class Meta:
        model = Radio
        fields = ('id', 'nome', 'programa_atual',)
    
    def programa_atual(self, obj):
        return obj.programa_atual()