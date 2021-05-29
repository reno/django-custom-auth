from django.test import TestCase
from users.models import CustomUser
from users.tests.data import user_data
from users.tokens import email_verification_token


class TokensTestCase(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(**user_data)
        self.token = email_verification_token.make_token(self.user)

    def test_encode(self):
        token = email_verification_token.make_token(self.user)
        self.assertEqual(self.token, token)

    def test_decode(self):
        self.assertTrue(email_verification_token.check_token(self.user, self.token))

