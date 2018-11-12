from django.test import TestCase
from django.test import Client
from django.urls import include, path, reverse, resolve
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from datetime import datetime
from apps.radio.models.programa import Programa
from apps.radio.models.radio import Radio
class ProgramaTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        
        cls.programa = Programa.objects.create(
            nome='Programa Teste', 
            categoria=1, 
            radio=Radio.objects.create(nome='Grade Teste'),
        )
        

    def test_nome_content(self):
        programa = Programa.objects.get(id=1)
        expected_object_name = f'{programa.nome}'
        self.assertEquals(expected_object_name, 'Programa Teste')

    def test_list_programa(self):
        response = self.client.get('/api/programa/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Programa Teste')

    def test_get_programa(self):
        response = self.client.get(reverse('programa-detail', args=[self.programa.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Programa Teste')

    def test_get_programa_error_404(self):

        response = self.client.get(reverse('programa-detail', args=[self.programa.id + 1]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['detail'] , "Não encontrado.")