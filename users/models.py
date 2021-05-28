from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

class CustomUser(AbstractUser):
    '''Custom user model.

    CustomUser inherits the following fields from AbstractUser:
    username, first_name, last_name, is_staff, date_joined

    The fields bellow are overwritten to allow login with email
    and email confirmation.
    '''
    email = models.EmailField(
        _('email address'),
        unique=True,
        error_messages = {'unique': _("This email is already registered.")},
    )
    is_active = models.BooleanField(_('is active'), default=False)
    # Add other user fields here

    def __str__(self):
        return self.username


