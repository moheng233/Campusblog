from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as authUserAdmin
from django.utils.translation import gettext, gettext_lazy as _

from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(authUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('avatar', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    list_display = ('username', 'email', 'last_name', 'is_staff')

    pass