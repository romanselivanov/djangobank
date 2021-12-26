from django.test import TestCase
from django.contrib.auth import get_user_model
from nezbank.models import Account, AccountType
import factory
from django.db.models import signals
from time import sleep
from django.utils import timezone


class UsersManagersTests(TestCase):

    @factory.django.mute_signals(signals.post_save, signals.pre_save)
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='normal@user.com', 
            phone='9005020', 
            password='FooPass500'
            )
        self.assertEqual(user.email, 'normal@user.com')
        self.assertEqual(user.phone, '9005020')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
    def test_create_account(self):
        User = get_user_model()
        customer = User.objects.create_user(
            email='normal@user.com', 
            phone='9005020', 
            password='FooPass500'
            )
        account_type = AccountType.objects.create(
            currency='US Dollar', 
            value=73.5
            )
        account = Account.objects.create(
            customer_id=customer, 
            description='test account', 
            created_at=timezone.now(),
            rate=1000.5,
            type=account_type
            )
        self.assertEqual(account.customer_id, customer)
        self.assertEqual(account.description, 'test account')
        self.assertEqual(account.rate, 1000.5)
        self.assertEqual(account.type, account_type)
