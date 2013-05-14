from django.test import TestCase, Client
import json
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils import unittest


class ExperienceDelete(TestCase):
    """ (no docs)
    """
    fixtures = ['all_data.json']

    def setUp(self):
        self.client = Client()
        self.user = User.objects.filter(username='admin')

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
    fixtures = ['all_data.json']

    def setUp(self):
        self.client = Client()
        self.user = User.objects.filter(username='admin')

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
    fixtures = ['all_data.json']

    def setUp(self):
        self.client = Client()
        self.user = User.objects.filter(username='admin')

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


        ########################################## da completare ##############################################
class ExperiencePreview(TestCase):
    """ Here we have to test the experience_preview view (found at webinator/views.py)
        1. is there the user?
        2. is there the experience?
        3. the 'if' works? (test it in all the possible cases)
    """
    fixtures = ['all_data.json']

    def setUp(self):
        self.client = Client()
        self.user = User.objects.filter(username='admin')

    def test_unexisting_experience(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('preview', kwargs={'uidb36':'12','token':'asddqadwerwerfAWE234536TY4'}))
        self.assertEquals(response.status_code, 404)

    def test_without_user(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get('preview')

        self.assertEquals(response.status_code, 403)

    ########################################################################################################

class ActionList(TestCase):
    """ Here we have to test the action_list view (found at webinator/views.py)
        1. is there the experience?
    """
    fixtures = ['all_data.json']

    def setUp(self):
        self.client = Client()

    def test_unexisting_experience(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('action_list', kwargs={'experience_id': '8'}))
        self.assertEquals(response.status_code, 404)

    def test_existing_experience(self):
        self.client.login(username='admin', password='admin')
        import pdb;pdb.set_trace()
        response = self.client.get(reverse('action_list', kwargs={'experience_id': '1'}))
        self.assertEquals(response.status_code, 200)


class QRCodeGenerator(TestCase):
    """ Here we have to test the qr_code_generator view (found at webinator/views.py)
        TODO[panizza]: questa la faccio io, e' un casino da spiegare e forse sara' da cambiare
    """


class Index(TestCase):
    """ Here we have to test the index view (found at webinator/views.py)
        1. check only if we have status_code == 200
    """
    def setUp(self):
        self.client = Client()
        self.user = User.objects.filter(username='admin')

    def test_it_works(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)


class ResetPasswordNewUser(TestCase):
    """ Here we have to test the reset_password_new_user view (found at webinator/views.py)
    """
