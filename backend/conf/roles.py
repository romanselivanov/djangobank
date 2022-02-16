from rolepermissions.roles import AbstractUserRole


class ViewAllAccounts(AbstractUserRole):
    available_permissions = {
        'view_all_accounts': True,
    }


class ViewSelfAccounts(AbstractUserRole):
    available_permissions = {
        'view_self_accounts': True,
    }
