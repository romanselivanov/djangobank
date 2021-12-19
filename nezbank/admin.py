from django.contrib import admin
from .models import User, Account, AccountType
from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm, UserCreationForm

@admin.register(User)
class AccountAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'phone', 'date_joined', 'is_active')

    fieldsets = (
        (None, 
        {'fields': (
            'email', 
            'password', 
            'phone', 
            'email_status'
            )}),
        ('Personal info', 
        {'fields': (
            'first_name', 
            'last_name', 
            'patronymic_name', 
            'date_joined', 
            'is_active',
            )}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(Account)
admin.site.register(AccountType)