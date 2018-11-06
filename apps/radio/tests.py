from django.test import TestCase
from django.urls import reverse

from .models import Radio


class RadioTests(TestCase):

    def setUp(self):
        Radio.objects.create(nome='Nova Radio')

    def test_nome_content(self):
        radio = Radio.objects.get(id=1)
        expected_object_name = f'{radio.nome}'
        self.assertEquals(expected_object_name, 'Nova Radio')

    def test_post_list_view(self):
        import pdb ; pdb.set_trace()
        response = self.client.get(reverse('/api/radio/'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'just a test')