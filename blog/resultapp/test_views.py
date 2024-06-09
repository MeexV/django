from django.test import Client, TestCase
from usersapp.models import ParsUser
class OpenViewsTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/contacts/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/result/')
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/vacancies/')
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/vacancies1/')
        self.assertEqual(response.status_code, 404)

    def test_login(self):
        ParsUser.objects.create_user(username='test_user', email='test@test.com',password='1234')
        response = self.client.get('/vacancies/')
        self.assertEqual(response.status_code, 302)
        self.client.login(username='test_user', password='1234')
        response = self.client.get('/vacancies/')
        self.assertEqual(response.status_code, 200)

