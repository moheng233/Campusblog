from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as authUserAdmin

from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(authUserAdmin):
    pass