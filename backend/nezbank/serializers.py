from rest_framework import serializers
from .models import Account, AccountType
from dj_rest_auth.serializers import LoginSerializer as DefaultLoginSerializer
from dj_rest_auth.serializers import (
    PasswordResetSerializer as DefaultPasswordResetSerializer)
from dj_rest_auth.serializers import (
    PasswordResetConfirmSerializer as DefaultPasswordResetConfirmSerializer)
from .services import token_generator
from django.conf import settings
from django.utils.http import urlsafe_base64_decode as uid_decoder
from django.utils.encoding import force_str
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError


UserModel = get_user_model()


class LoginSerializer(DefaultLoginSerializer):
    email = None


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('rate', 'type', 'description')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['customer_id'] = user
        instance = super(AccountSerializer, self).create(validated_data)
        return instance

    def update(self, instance, validated_data):
        user = self.context['request'].user
        validated_data['customer_id'] = user
        instance = super(AccountSerializer, self).update(
            instance, validated_data
        )
        return instance


class AccountTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountType
        fields = '__all__'


class VerificationCodeSerializer(serializers.Serializer):
    token = serializers.CharField(required=True, max_length=6, min_length=6)


class PasswordResetSerializer(DefaultPasswordResetSerializer):
    def get_email_options(self):
        return {
            'html_email_template_name': 'email/reset-password.html',
        }

    def save(self):
        request = self.context.get('request')
        opts = {
            'use_https': request.is_secure(),
            'from_email': getattr(settings, 'DEFAULT_FROM_EMAIL'),
            'request': request,
            'token_generator': token_generator,
        }
        opts.update(self.get_email_options())
        self.reset_form.save(**opts)


class PasswordResetConfirmSerializer(DefaultPasswordResetConfirmSerializer):

    def validate(self, attrs):
        try:
            uid = force_str(uid_decoder(attrs['uid']))
            self.user = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            raise ValidationError({'uid': ['Invalid value']})

        if not token_generator.check_token(self.user, attrs['token']):
            raise ValidationError({'token': ['Invalid value']})

        self.custom_validation(attrs)
        self.set_password_form = self.set_password_form_class(
            user=self.user, data=attrs,
        )
        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)

        return attrs
