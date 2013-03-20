from django.test import TestCase, Client

class PasswordStuffTest(TestCase):
    #fixtures=[]
    def setUp(self):
        self.client = Client()