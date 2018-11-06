from rest_framework import generics, viewsets, views
from apps.core.views import PermissionTokenLoginRequiredMixin
from .models import Radio, Programa, Programacao
from .serializers import RadioSerializer, ProgramaSerializer, ProgramacaoSerializer
from .filters import ProgramaFilter

class RadioViewSet(viewsets.ModelViewSet):
    queryset = Radio.objects.all()
    serializer_class = RadioSerializer


class ProgramaViewSet(viewsets.ModelViewSet):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer
    

    def get_queryset(self):
        queryset = self.queryset
        radio_id = self.request.GET.get('radio', None)
        
        if radio_id:
            queryset = queryset.filter(radio=radio_id)
        
        return queryset


class ProgramacaoViewSet(viewsets.ModelViewSet):
    queryset = Programacao.objects.all()
    serializer_class = ProgramacaoSerializer
