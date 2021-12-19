from django.contrib.auth.base_user import BaseUserManager
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.hashers import make_password

from django.core.exceptions import ValidationError
from django.utils.translation import gettext

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone, email, password, **extra_fields):
        """
        Create and save a user with the given phone, email, and password.
        """
        if not phone:
            raise ValueError('Phone must be set')
        if not email: 
            raise ValueError('Email must be set')

        email = self.normalize_email(email)
        user = self.model(phone=phone, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, email, password, **extra_fields)

    def create_superuser(self, phone, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(phone, email, password, **extra_fields)

    def get_by_natural_key(self, username):
        return self.get(
            Q(**{self.model.USERNAME_FIELD: username}) |
            Q(**{self.model.PHONE_FIELD: username})
        )


class PasswordCharsValidator:
    """
    Validate whether the password has upper, lower and digit.
    """
    def validate(self, password, user=None):

        if not any(char.isdigit() for char in password):
            raise ValidationError(
                gettext('Password should have at least one numeral'),
                code='password_nothave_numeral',)
         
        if not any(char.isupper() for char in password):
            raise ValidationError(
                gettext('Password should have at least one uppercase letter'),
                code='password_nothave_uppercase',)
            
        if not any(char.islower() for char in password):
            raise ValidationError(
                gettext('Password should have at least one lowercase letter'),
                code='password_nothave_lowercase',)

    def get_help_text(self):
        return gettext("Your password must contain at least character.",)
