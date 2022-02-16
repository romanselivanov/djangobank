from rest_framework.viewsets import GenericViewSet
from nezbank.authutils import NezbankModelPermission
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    AccountSerializer, AccountTypeSerializer, VerificationCodeSerializer
    )
from nezbank.models import Account, AccountType
from rest_framework.decorators import action
from rest_framework.response import Response
from .filters import AccountPermissionFilter
from .models import User
from .services import token_generator
from django.utils.translation import gettext_lazy as _
from rest_framework.mixins import (
    CreateModelMixin, RetrieveModelMixin, ListModelMixin
)


class AccountsView(
    CreateModelMixin, RetrieveModelMixin, ListModelMixin, GenericViewSet
    ):
    # serializers = {
    #     'default': AccountSerializer,
    #     'accounttypes_list': AccountTypeSerializer,
    #     }
    serializer_class = AccountSerializer
    filter_backends = (AccountPermissionFilter,)
    queryset = Account.objects.all()
    permission_classes = [NezbankModelPermission]


class AccountTypeView(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = AccountTypeSerializer
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        return AccountType.objects.filter(accounts=self.kwargs['pk'])


class EmailVerificationView(GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = VerificationCodeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        token = token_generator.check_token(
            user=user,
            token=serializer.data['token']
            )
        if token:
            user.email_status = User.EmailStatus.VERIFIED
            user.save()
            return Response({'detail': _('Email verified')},)
        else:
            return Response(
                {'detail': _('Entered digits incorrect')},
                status=400
                )
