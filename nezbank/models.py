from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE, DO_NOTHING
from .authutils import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from rolepermissions.roles import get_user_roles
import inflection
from django.utils.functional import cached_property


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
        error_messages={'unique': _(
            "A user with that phone already exists.")}
        )

    email = models.EmailField(
        _('email address'),
        unique=True,
        error_messages={'unique': _("A user with that email already exists.")}
        )
    patronymic_name = models.CharField(
        _('Отчество'),
        max_length=150,
        blank=True
        )
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

    @cached_property
    def roles(self):
        try:
            return [inflection.underscore(role.__name__) for role in get_user_roles(self)]
        except Exception:
            return ''

    def save(self, **kwargs):
        if self.email_status != self.EmailStatus.NOT_VERIFIED:
            old_user = User.objects.get(id=self.id)
            if old_user.email != self.email:
                self.email_status = self.EmailStatus.NOT_VERIFIED
                super(User, self).save(**kwargs)

        super(User, self).save(**kwargs)


class VerifyCode(models.Model):
    customer = models.ForeignKey(
        User,
        related_name='otp',
        on_delete=CASCADE,
        verbose_name="Клиент"
        )
    code = models.CharField(max_length=6, blank=False, null=True)
    created = models.DateTimeField(default=timezone.now)

    def save(self, **kwargs):
        self.__class__.objects.filter(customer=self.customer).delete()
        super(VerifyCode, self).save(**kwargs)


class AccountType(models.Model):
    id = models.BigIntegerField(primary_key=True)
    currency = models.CharField(max_length=50, verbose_name="Валюта")
    value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Курс"
        )

    def __str__(self):
        return self.currency


class Account(models.Model):
    customer = models.ForeignKey(
        User,
        related_name='accounts',
        on_delete=DO_NOTHING,
        verbose_name="Клиент"
        )
    description = models.CharField(max_length=250, verbose_name="Описание")
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="Дата создания аккаунта"
        )
    rate = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Средств на счете")
    type = models.ForeignKey(
        AccountType,
        on_delete=DO_NOTHING,
        verbose_name="Тип валюты",
        related_name='accounts'
        )

    def __str__(self):
        return self.customer.email
