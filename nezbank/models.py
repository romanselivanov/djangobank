from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import DO_NOTHING
from .authutils import CustomUserManager
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    class EmailStatus(models.TextChoices):
        NOT_VERIFIED = 'not_verified', 'Не верифицирован'
        EMAIL_SENT = 'email_sent', 'Письмо с подтверждением отправлено'
        VERIFIED = 'verified', 'Верифицирован'

    username = None
    phone = models.CharField(
        _('phone'), 
        max_length=50, 
        unique=True, 
        error_messages={'unique': _("A user with that phone already exists."),}
        )

    email = models.EmailField(
        _('email address'), 
        unique=True,
        error_messages={'unique': _("A user with that email already exists."),}
        )
    patronymic_name = models.CharField(_('Отчество'), max_length=150, blank=True)
    email_status = models.CharField(
        verbose_name='Статус email',
        max_length=32,
        choices=EmailStatus.choices,
        default=EmailStatus.NOT_VERIFIED
    )

    USERNAME_FIELD = 'email'
    PHONE_FIELD = 'phone'
    REQUIRED_FIELDS = ['phone']

    objects = CustomUserManager()

    def save(self, **kwargs):
        if self.email_status != self.EmailStatus.NOT_VERIFIED:
            old_user = User.objects.get(id=self.id)
            if old_user.email != self.email:
                self.email_status = self.EmailStatus.NOT_VERIFIED
                super(User, self).save(**kwargs)
                
        super(User, self).save(**kwargs)


class AccountType(models.Model):
    currency = models.CharField(max_length=50)
    value = models.FloatField()

    def __str__(self):
        return self.currency


class Account(models.Model):
    customer_id = models.ForeignKey(User, on_delete=DO_NOTHING)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField()
    rate = models.FloatField()
    type = models.ForeignKey(AccountType, on_delete=DO_NOTHING)

    def __str__(self):
        return self.description
