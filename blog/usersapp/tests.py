from django.test import TestCase
from mixer.backend.django import mixer
from django.contrib.auth import get_user_model

ParsUser = get_user_model()

class TestParsUser(TestCase):

    def setUp(self):
        self.user = mixer.blend(ParsUser, username='test_user', email='test@test.com')

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'test_user')
        self.assertEqual(self.user.email, 'test@test.com')

    def test_email_unique(self):
        with self.assertRaises(Exception):
            mixer.blend(ParsUser, username='testuser2', email='test@test.com')
