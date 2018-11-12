from django.test import TestCase
from django.test import Client
from django.urls import include, path, reverse, resolve
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase

from apps.radio.models.radio import Radio

class RadioTestCase(TestCase):

    def setUp(self):
        self.radio = Radio.objects.create(nome='Nova Radio')

    def test_nome_content(self):
        radio = Radio.objects.get(id=1)
        expected_object_name = f'{radio.nome}'
        self.assertEquals(expected_object_name, 'Nova Radio')


    def test_list_radio(self):
        
        response = self.client.get(reverse('radio-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['nome'] , 'Nova Radio')

    def test_get_radio(self):

        response = self.client.get(reverse('radio-detail', args=[self.radio.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'] , 'Nova Radio')

    def test_get_radio_error(self):

        response = self.client.get(reverse('radio-detail', args=[self.radio.id + 1]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['detail'] , "Não encontrado.")