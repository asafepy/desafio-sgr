from rest_framework import generics, viewsets, views
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.core.views import PermissionTokenLoginRequiredMixin
from .models.radio import Radio
from .models.programa import Programa
from .models.programacao import GradeProgramacao, Grade
from .serializers import (RadioSerializer, 
                          ProgramaSerializer, 
                          GradeSerializer, 
                          ProgramaAtualSerializer)
from .filters import ProgramaFilter
from django.db.models import Q



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
        serializer = GradeSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Grade.objects.all()
        grade = get_object_or_404(queryset, pk=pk)
        serializer = GradeSerializer(grade, context={'request': request})
        return Response(serializer.data)

class ProgramaAtualViewSet(viewsets.ModelViewSet):
    queryset = Radio.objects.all()
    serializer_class = ProgramaAtualSerializer

    def get_queryset(self):
        queryset = self.queryset
        radio_id = self.request.GET.get('radio', None)
        
        if radio_id:
            queryset = queryset.filter(radio=radio_id)
        
        return {}




# class RadioViewSet(viewsets.ViewSet):
     
#     def list(self, request):
#         queryset = Programa.objects.all()
#         serializer = ProgramaSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = Programa.objects.all()
#         programa = get_object_or_404(queryset, pk=pk)
#         serializer = RadioSerializer(programa, context={'request': request})
#         return Response(serializer.data)



# class RadioViewSet(viewsets.ViewSet):
     
#     def list(self, request):
#         queryset = Programa.objects.all()
#         serializer = ProgramaSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = Programa.objects.all()
#         programa = get_object_or_404(queryset, pk=pk)
#         serializer = RadioSerializer(programa, context={'request': request})
#         return Response(serializer.data)

# class ProgramaViewList(generics.ListAPIView):
#     model = Programa
#     queryset = Programa.objects.all()
#     serializer_class = ProgramaSerializer

#     search_fields = ('title', 'title_en', 'description', 'description_en', 'type__title','tags__name', 'author__slug', 'areas_expertise__title', 'type__title_en', 'areas_expertise__title_en')

# class ProgramaViewSet2(viewsets.ModelViewSet):
#     queryset = Programa.objects.all()
#     serializer_class = ProgramaSerializer

#     def get_queryset(self):
#         queryset = self.queryset
#         radio_id = self.request.GET.get('radio', None)
        
#         if radio_id:
#             queryset = queryset.filter(radio=radio_id)
        
#         return queryset

# class GradeProgramacaoViewSet(viewsets.ModelViewSet):
#     queryset = Grade.objects.all()
#     serializer_class = GradeProgramacaoSerializer

# class ProgramaAtualViewSet(viewsets.ModelViewSet):
#     queryset = Radio.objects.all()
#     serializer_class = ProgramaAtualSerializer

#     def get_queryset(self):
#         queryset = self.queryset
#         radio_id = self.request.GET.get('radio', None)
        
#         if radio_id:
#             queryset = queryset.filter(radio=radio_id)
        
#         return {}