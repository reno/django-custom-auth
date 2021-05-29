from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(UserManager):
    '''Custom user manager. Extends de default UserManager.'''

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return super()._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return super()._create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    '''Custom user model.

    CustomUser inherits the following fields from AbstractUser:
    username, first_name, last_name, is_staff, is_superuser, date_joined

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

    objects = CustomUserManager()

    def __str__(self):
        return self.username


