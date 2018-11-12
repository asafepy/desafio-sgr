from django.test import TestCase
from django.test import Client
from django.urls import include, path, reverse, resolve
from rest_framework import status
from datetime import datetime

from apps.radio.models.programacao import Grade, GradeProgramacao
from apps.radio.models.radio import Radio
from apps.radio.models.programa import Programa

class GradeListViewTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        
        cls.grade = Grade.objects.create(
            data_exibicao = datetime.now(),
            radio = Radio.objects.create(nome='Grade Teste'),
        )

        cls.grade_programacao = GradeProgramacao.objects.create(
            horario_inicio = datetime.now(),
            horario_fim = datetime.now(),
            programa = Programa.objects.create(nome='Programa Teste', categoria=1),
            grade = cls.grade,
        )
           
    def test_list_url_exists_at_desired_location(self):
        response = self.client.get('/api/grade/')
        self.assertEqual(response.status_code, 200)
           
    def test_list_url_accessible_by_name(self):
        response = self.client.get(reverse('grade-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Grade Teste')
        
    def test_list_grade_correct_response(self):
        response = self.client.get(reverse('grade-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Grade Teste')

    def test_detail_url_exists_at_desired_location(self):
        # import pdb; pdb.set_trace()
        response = self.client.get(reverse('grade-detail', args=[self.grade.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Grade Teste')
        self.assertContains(response, 'grade')
           
    def test_detail_url_accessible_by_name(self):
        response = self.client.get(reverse('grade-detail', args=[self.grade.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Grade Teste')
        
    def test_detail_grade_correct_response(self):
        response = self.client.get(reverse('grade-detail', args=[self.grade.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Grade Teste')
        self.assertContains(response, 'grade')

    def test_detail_get_grade_error_404(self):
        response = self.client.get(reverse('grade-detail', args=[self.grade.id + 1]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['detail'] , "Não encontrado.")