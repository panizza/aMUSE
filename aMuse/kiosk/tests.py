from django.test import TestCase, Client
from basetyzer.models import Exhibit
from django.core.urlresolvers import reverse
import json as j

class HomeTest(TestCase):
    """ no docs
    """
    fixtures = ['all_data.json']

    def setUp(self):
        self.client = Client()

    def test_right_get_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


class ExhibitItemListTest(TestCase):
    """ no docs
    """
    fixtures = ['all_data.json']

    def setUp(self):
        self.client = Client()

    def test_wrong_method(self):
        response = self.client.post(reverse('exhibit_item_list', kwargs={'id_exhibition': '1'}), data={})
        self.assertEquals(response.status_code, 405)

    def test_unexisting_exhbition(self):
        response = self.client.get(reverse('exhibit_item_list', kwargs={'id_exhibition': '99999'}))
        self.assertEquals(response.status_code, 404)

    def test_right_request(self):
        response = self.client.get(reverse('exhibit_item_list', kwargs={'id_exhibition': '1'}))
        self.assertEquals(response.status_code, 200)


class ItemInfoTest(TestCase):
    """ no docs
    """
    fixtures = ['all_data.json']

    def setUp(self):
        self.client = Client()

    def test_wrong_method(self):
        response = self.client.post(reverse('item_info', kwargs={'id_item': '1'}), data={})
        self.assertEquals(response.status_code, 405)

    def test_unexisting_item(self):
        response = self.client.get(reverse('item_info', kwargs={'id_item': '99999'}))
        self.assertEquals(response.status_code, 404)

    def test_right_request(self):
        response = self.client.get(reverse('item_info', kwargs={'id_item': '1'}))
        self.assertEquals(response.status_code, 200)


class ExhibitionListTest(TestCase):
    """ no docs
    """
    def setUp(self):
        self.client = Client()

    def test_wrong_method(self):
        response = self.client.post(reverse('exhibition_list'), data={})
        self.assertEquals(response.status_code, 405)

    def test_right_request(self):
        response = self.client.get(reverse('exhibition_list'))
        self.assertEquals(response.status_code, 200)