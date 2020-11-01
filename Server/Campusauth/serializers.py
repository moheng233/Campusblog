from django.contrib.auth import get_user_model
from django.db.models import fields
from djoser.conf import settings
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from djoser.serializers import UserSerializer;
from django.contrib.auth.models import User, models

from drf_extra_fields.fields import Base64ImageField

User = get_user_model()

class UserSerializer(UserSerializer):
    avatar = Base64ImageField()

    class Meta:
        model = User
        fields = (
            "id",
            "last_login",
            "username",
            "first_name",
            "last_name",
            "email",
            'avatar'
        )
        read_only_fields = (settings.LOGIN_FIELD,)