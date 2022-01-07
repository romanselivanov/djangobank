from rest_framework.viewsets import ModelViewSet, GenericViewSet
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
from .services import code_generator


class AccountsView(ModelViewSet):
    serializers = {
        'default': AccountSerializer,
        'accounttypes_list': AccountTypeSerializer,
        }
    filter_backends = (AccountPermissionFilter,)

    def get_queryset(self):
        if self.action == 'accounttypes_list':
            return AccountType.objects.all()
        else:
            return Account.objects.all()

    def get_permissions(self):
        if self.action == 'accounttypes_list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [NezbankModelPermission]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        return self.serializers.get(
            self.action,  self.serializers['default']
        )

    @action(methods=['get'], url_path='accountypes', detail=False)
    def accounttypes_list(self, request, **kwargs):
        accounttypes = self.get_queryset()
        serializer = self.get_serializer(accounttypes, many=True)
        return Response(serializer.data)


class EmailVerificationView(GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = VerificationCodeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        code = code_generator.check_token(user=user, token=serializer.data['code'])
        if code:
            user.email_status = User.EmailStatus.VERIFIED
            user.save()
            return Response(status=200)
        else:
            return Response(status=400)
