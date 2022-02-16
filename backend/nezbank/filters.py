from rest_framework.filters import BaseFilterBackend
# from django.db import connection


class AccountPermissionFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        user = request.user
        # print(len(connection.queries))
        if 'view_all_accounts' in user.roles:
            return queryset

        return queryset.filter(customer=request.user)
