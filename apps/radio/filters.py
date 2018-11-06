import django_filters
from .models import Programa

class ProgramaFilter(django_filters.FilterSet):
    class Meta:
        model = Programa
        fields = ['nome']