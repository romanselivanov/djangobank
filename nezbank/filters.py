from rest_framework.filters import BaseFilterBackend


def accounts_view_all(user):
    return user.groups.filter(name='accounts_view_all').exists()


def account_self(user):
    return user.groups.filter(name='account_self').exists()


class AccountPermissionFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        user = request.user
        if accounts_view_all(user):
            return queryset

        return queryset.filter(customer=user)
