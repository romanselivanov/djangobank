from django.test import TestCase
from django.contrib.auth import get_user_model


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', phone='9539005020', password='FooPass500')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertEqual(user.phone, '9539005020')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
    
    # def test_create_superuser(self):
    #     User = get_user_model()
    #     admin_user = User.objects.create_superuser('super@user.com', 'FooPass500')
    #     self.assertEqual(admin_user.email, 'super@user.com')
    #     self.assertTrue(admin_user.is_active)
    #     self.assertTrue(admin_user.is_staff)
    #     self.assertTrue(admin_user.is_superuser)
    #     try:
    #         # username is None for the AbstractUser option
    #         # username does not exist for the AbstractBaseUser option
    #         self.assertIsNone(admin_user.username)
    #     except AttributeError:
    #         pass
    #     with self.assertRaises(ValueError):
    #         User.objects.create_superuser(
    #             email='super@user.com', password='FooPass500', is_superuser=False)
