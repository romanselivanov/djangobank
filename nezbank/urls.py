from django.urls import path, include
from nezbank.views import AccountsView
from rest_framework import routers


api_router = routers.DefaultRouter()
api_router.register(r'accounts', AccountsView, basename='accounts')


urlpatterns = [
    path('', include(api_router.urls)),
]
