from django.contrib.auth import get_user_model
from django.core import mail
from django.template.loader import render_to_string
from django.test import TestCase
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from users.forms import CustomUserCreationForm
from users.tests.data import user_data, user_form_data
from users.tokens import email_verification_token


class CustomUserCreationFormTestCase(TestCase):

    def test_valid_data(self):
        # Fix form throwing validation error even with valid data
        user_form_data['password2'] = user_form_data['password1']
        form = CustomUserCreationForm(data=user_form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        user_form_data['password2'] = 'error'
        form = CustomUserCreationForm(data=user_form_data)
        self.assertFalse(form.is_valid())

    def test_send_confirmation_email(self):
        UserModel = get_user_model()
        user = UserModel.objects.create_user(**user_data)
        domain = 'test'
        form = CustomUserCreationForm()
        message = render_to_string(
            'registration/email_confirmation_message.html', {
                'user': user,
                'domain': domain,
                'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': email_verification_token.make_token(user),
            }
        )
        form.send_confirmation_email(user, domain)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Django app account verification')
        self.assertEqual(mail.outbox[0].body, message)