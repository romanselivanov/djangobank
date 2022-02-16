from django.urls import path, include
from nezbank.views import AccountsView, EmailVerificationView, AccountTypeView
import conf.routers as routers


router = routers.DefaultRouter()
router.register(r'accounts', AccountsView, basename='accounts')
router.register(r'auth/email-verification', EmailVerificationView, basename='email_verification')

accounts_router = routers.NestedDefaultRouter(router, r'accounts', lookup='accounts')
accounts_router.register(r'accounttypes', AccountTypeView, basename='accounttypes')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(accounts_router.urls)),
]
