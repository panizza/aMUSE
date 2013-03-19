from django.test import TestCase, Client
from basetyzer.models import Exhibit
import json as j

class ExhibitionTest(TestCase):
    fixtures = ['test.json']
    def setUp(self):
        self.client = Client()

    def test_exhibitions_list(self):
        response = self.client.get('/api/e/')
        self.assertEqual(response.status_code, 200)
        json = j.loads(response.content)
        self.assertEqual(len(json['data']), 2)

    def test_exhibition_info(self):
        response = self.client.get('/api/e/54326435842647/')
        self.assertEqual(response.status_code, 404)
        response = self.client.get('/api/e/1/')
        self.assertEqual(response.status_code, 200)


class ItemTest(TestCase):
    fixtures = ['test.json']
    def setUp(self):
        self.client = Client()

    def test_item_list(self):
        response = self.client.get('/api/e/43265435756867/i/')
        self.assertEqual(response.status_code, 404)
        response = self.client.get('/api/e/1/i/')
        self.assertEqual(response.status_code, 200)
        json = j.loads(response.content)
        self.assertTrue(json.get('data'))


    def test_get_item_info(self):
        response = self.client.get('/api/i/43265435756867/')
        self.assertEqual(response.status_code, 404)
        response = self.client.get('/api/i/1/')
        self.assertEqual(response.status_code, 200)
