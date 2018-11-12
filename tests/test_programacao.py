from django.test import TestCase
from django.test import Client
from django.urls import include, path, reverse, resolve
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from datetime import datetime
from apps.radio.models.radio import Radio
from apps.radio.models.programa import Programa
from apps.radio.models.programacao import Programacao

class ProgramacaoTestCase(TestCase):

    def setUp(self):
        radio = Radio.objects.create(nome='Nova Radio')
        programa = Programa.objects.create(nome='Programa Teste', categoria='futebol', horario_exibicao=datetime.now())
        Programacao.objects.create(nome='Programacao Teste', radio=radio, data_exibicao=datetime.now())
        
    def test_nome_content(self):
        programacao = Programacao.objects.get(id=1)
        expected_object_name = f'{programacao.nome}'
        self.assertEquals(expected_object_name, 'Programacao Teste')


    def test_list_programacao(self):
        
        response = self.client.get('/api/programacao/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['nome'] , 'Programacao Teste')

    def test_get_programacao(self):

        response = self.client.get('/api/programacao/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'] , 'Programacao Teste')

    def test_get_programacao_error(self):

        response = self.client.get('/api/programacao/2/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['detail'] , "Não encontrado.")