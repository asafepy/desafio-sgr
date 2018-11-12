from django.test import TestCase
from django.test import Client
from django.urls import include, path, reverse, resolve
from rest_framework import status
from datetime import datetime

from apps.radio.models.programacao import Grade, GradeProgramacao
from apps.radio.models.programa import Programa
from apps.radio.models.radio import Radio



class GradeListViewTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        
        cls.grade_programacao = GradeProgramacao.objects.create(
            horario_inicio = datetime.now(),
            horario_fim = datetime.now(),
            programa = Programa.objects.create(nome='Programa Teste', categoria=1),
            grade = Grade.objects.create(data_exibicao = datetime.now(), radio = Radio.objects.create(nome='Nova Radio')),
        )
           
    # def test_view_url_exists_at_desired_location(self):
    #     response = self.client.get('/api/grade/')
    #     self.assertEqual(response.status_code, 200)
           
    # def test_view_url_accessible_by_name(self):
    #     response = self.client.get(reverse('grade-detail'))
    #     self.assertEqual(response.status_code, 200)
        
    # def test_view_grade_correct_response(self):
    #     response = self.client.get(reverse('grade-detail'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'Nova Radio')
        
    # def test_get_grade_error_404(self):
    #     response = self.client.get(reverse('grade-detail', args=[self.grade.id + 1]))
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    #     self.assertEqual(response.data['detail'] , "Não encontrado.")