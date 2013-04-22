from django.test import TestCase, Client
import json
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils import unittest


class ExperienceDelete(TestCase):
    """ (no docs)
    """
    fixtures = ['test_only.json']

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(username='admin', password='admin', email='admin@example.com')

    def test_unauthorized(self):
        response = self.client.get(reverse('delete_experience', kwargs={'experience_id': '1'}))
        self.assertEquals(response.status_code, 401)

    def test_wrong_request(self):
        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse('delete_experience', kwargs={'experience_id': '1'}), data={})
        self.assertEquals(response.status_code, 405)

    def test_existing_experience(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('delete_experience', kwargs={'experience_id': '1'}))
        self.assertEquals(response.status_code, 200)
        resp = json.loads(response.content)
        self.assertEquals(resp['status'], 'deleted')

    def test_unexisting_experience(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('delete_experience', kwargs={'experience_id': '6'}))
        self.assertEquals(response.status_code, 404)


class ActionDelete(TestCase):
    """ (no docs)
    """
    fixtures = ['test_only.json']

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(username='admin', password='admin', email='admin@example.com')

    def test_unauthorized(self):
        response = self.client.get(reverse('delete_action', kwargs={'action_id': '1'}))
        self.assertEquals(response.status_code, 401)

    def test_wrong_request(self):
        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse('delete_action', kwargs={'action_id': '1'}), data={})
        self.assertEquals(response.status_code, 405)

    def test_existing_action(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('delete_action', kwargs={'action_id': '1'}))
        self.assertEquals(response.status_code, 200)
        resp = json.loads(response.content)
        self.assertEquals(resp['status'], 'deleted')

    def test_unexisting_action(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('delete_action', kwargs={'action_id': '6'}))
        self.assertEquals(response.status_code, 404)


class ActionEdit(TestCase):
    """ (no docs)
    """
    fixtures = ['test_only.json']

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(username='admin', password='admin', email='admin@example.com')

    def test_unauthorized(self):
        response = self.client.post(reverse('edit_action', kwargs={'action_id': '1'}), data={
            'comment': 'my new comment'
        })
        self.assertEquals(response.status_code, 401)

    def test_wrong_request(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('edit_action', kwargs={'action_id': '1'}))
        self.assertEquals(response.status_code, 405)

    def test_correct_action_and_post(self):
        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse('edit_action', kwargs={'action_id': '1'}), data={
            'comment': 'my new comment'
        })
        self.assertEquals(response.status_code, 200)
        resp = json.loads(response.content)
        self.assertEquals(resp['status'], 'updated')

    def test_wrong_action(self):
        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse('edit_action', kwargs={'action_id': '6'}), data={
            'comment': 'my new comment'
        })
        self.assertEquals(response.status_code, 404)

    def test_wrong_post(self):
        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse('edit_action', kwargs={'action_id': '1'}), data={})
        self.assertEquals(response.status_code, 404)
        resp = json.loads(response.content)
        self.assertEquals(resp['status'], 'error')


class ViewError(TestCase):
    """ (no docs)
    """
    def setUp(self):
        self.client = Client()

    def test_right_id(self):
        response = self.client.get(reverse('view_error', kwargs={'error_id': '1'}))
        self.assertEquals(response.status_code, 200)

    def test_wrong_id(self):
        response = self.client.get(reverse('view_error', kwargs={'error_id': '2'}))
        self.assertEquals(response.status_code, 404)
        response = self.client.get(reverse('view_error', kwargs={'error_id': '0'}))
        self.assertEquals(response.status_code, 404)

