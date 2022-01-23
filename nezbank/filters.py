from rest_framework.filters import BaseFilterBackend


class AccountPermissionFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        roles = request.user.roles
        if 'view_all_accounts' in roles:
            return queryset

        return queryset.filter(customer=request.user)
