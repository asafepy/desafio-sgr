from rest_framework import generics, viewsets, views
from apps.core.views import PermissionTokenLoginRequiredMixin
from .models.radio import Radio
from .models.programa import Programa
from .models.programacao import GradeProgramacao, Grade
from .serializers import (RadioSerializer, 
                          ProgramaSerializer, 
                          GradeProgramacaoSerializer, 
                          ProgramaAtualSerializer)
from .filters import ProgramaFilter
from django.db.models import Q


class ProgramaViewSet(viewsets.ModelViewSet):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer

    def get_queryset(self):
        queryset = self.queryset
        radio_id = self.request.GET.get('radio', None)
        
        if radio_id:
            queryset = queryset.filter(radio=radio_id)
        
        return queryset

class GradeProgramacaoViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeProgramacaoSerializer

class ProgramaAtualViewSet(viewsets.ModelViewSet):
    queryset = Radio.objects.all()
    serializer_class = ProgramaAtualSerializer

    def get_queryset(self):
        queryset = self.queryset
        radio_id = self.request.GET.get('radio', None)
        
        if radio_id:
            queryset = queryset.filter(radio=radio_id)
        
        return {}


class RadioViewSet(viewsets.ModelViewSet):
    queryset = Radio.objects.all()
    serializer_class = RadioSerializer