from rest_framework import serializers
from .models import Account, AccountType
from dj_rest_auth.serializers import LoginSerializer as DefaultLoginSerializer


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
