from django.contrib.auth.forms import UserCreationForm
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from users.models import CustomUser
from users.tokens import email_verification_token


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            'email', 'first_name', 'last_name', 'username', 'password1', 'password2'
        )

    def send_confirmation_email(self, user, domain):
        subject = 'Django app account verification'
        context = {
            'user': user,
            'domain': domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': email_verification_token.make_token(user),
        }
        message = render_to_string(
            'registration/email_confirmation_message.html', context
        )
        user.email_user(subject, message)