from django.urls import path, include
from nezbank.views import AccountsView, EmailVerificationView
from rest_framework import routers


api_router = routers.DefaultRouter()
api_router.register(r'accounts', AccountsView, basename='accounts')
api_router.register(r'auth/email-verification', EmailVerificationView, basename='email_verification')

urlpatterns = [
    path('', include(api_router.urls)),
]
