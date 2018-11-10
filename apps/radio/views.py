from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.core.views import PermissionTokenLoginRequiredMixin
from .models.radio import Radio
from .models.programa import Programa
from .models.programacao import GradeProgramacao, Grade
from .serializers import (RadioSerializer, 
                          GradeSerializer, 
                          GradeListSerializer,
                          ProgramaAtualSerializer,
                          ProgramaAtualListSerializer)


class RadioViewSet(viewsets.ViewSet):
     
    def list(self, request):
        queryset = Radio.objects.all()
        serializer = RadioSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Radio.objects.all()
        radio = get_object_or_404(queryset, pk=pk)
        serializer = RadioSerializer(radio, context={'request': request})
        return Response(serializer.data)

class GradeViewSet(viewsets.ViewSet):
     
    def list(self, request):
        queryset = Grade.objects.all()
        serializer = GradeListSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Grade.objects.all()
        grade = get_object_or_404(queryset, pk=pk)
        serializer = GradeSerializer(grade, context={'request': request})
        return Response(serializer.data)


class ProgramaAtualViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Radio.objects.all()
        serializer = ProgramaAtualListSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Radio.objects.all()
        programa_atual = get_object_or_404(queryset, pk=pk)
        serializer = ProgramaAtualSerializer(programa_atual, context={'request': request})
        return Response(serializer.data)
        