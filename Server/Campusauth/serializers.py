from Campusblogs.serializers import UploadImagesSerializer
from django.contrib.auth import get_user_model
from django.db.models import fields
from djoser.conf import settings
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from djoser.serializers import UserSerializer;
from django.contrib.auth.models import User, models

User = get_user_model()

class UserSerializer(UserSerializer):
    avatar = UploadImagesSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "last_login",
            "username",
            "last_name",
            "email",
            'avatar'
        )
        read_only_fields = (getattr(settings,'LOGIN_FIELD'),'last_login','id')

class SetUserAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","avatar")