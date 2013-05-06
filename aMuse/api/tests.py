from django.test import TestCase, Client
from basetyzer.models import Exhibit
from django.core.urlresolvers import reverse
import json as j


class ExhibitionTest(TestCase):
    fixtures = ['percussion.json', 'with_experience.json']

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
    fixtures = ['percussion_new_db.json', 'all_data.json']

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
        response = self.client.get('/api/i/356a192b7913b04c54574d18c28d46e6395428ab/')
        self.assertEqual(response.status_code, 200)


class ExperienceTest(TestCase):
    fixtures = ['percussion_new_db.json']

    def setUp(self):
        self.client = Client()

    def test_save_experience(self):
        """
        TODO[lotto]: moar failing test cases and image
        """

        #working case
        exp_dict = {"exp": [{"id": "2",
                             "date": "2013-05-06 17:42:52",
                             "photo": "",
                             "text": "ne voglio una",
                             "type": "scan"},
                            {"id": "1",
                             "date": "2013-05-06 17:43:30",
                             "photo": "",
                             "text": "master master",
                             "type": "scan"},
                            {"date": "2013-05-06 17:43:56",
                             "photo": "",
                             "text": "questi bonghi mi fanno venire voglia di africa",
                             "type": "personal"}],
                    "confirm": "24e3261d7bbe24664c1babc75189cfebec04498b",
                    "email": "gpinelli@brixen.de"}

        exp_json = j.dumps(exp_dict)

        response = self.client.post('/api/exp/s/', exp_json, content_type='application/json')
        self.assertEqual(response.status_code, 200)


        #bad confirmation code
        exp_dict = {"exp": [{"id": "2",
                             "date": "2013-05-06 17:42:52",
                             "photo": "",
                             "text": "ne voglio una",
                             "type": "scan"},
                            {"id": "1",
                             "date": "2013-05-06 17:43:30",
                             "photo": "",
                             "text": "master master",
                             "type": "scan"},
                            {"date": "2013-05-06 17:43:56",
                             "photo": "",
                             "text": "questi bonghi mi fanno venire voglia di africa",
                             "type": "personal"}],
                    "confirm": "347523459836932475294529",
                    "email": "gpinelli@brixen.de"}

        exp_json = j.dumps(exp_dict)

        response = self.client.post('/api/exp/s/', exp_json, content_type='application/json')

        self.assertEqual(response.status_code, 400)
