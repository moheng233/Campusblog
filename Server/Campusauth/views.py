from Campusblogs.models import UploadImages
from django.contrib.auth import get_user_model
from django.shortcuts import render
from djoser.views import UserViewSet as djoserUserViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from Campusauth.serializers import SetUserAvatarSerializer

User = get_user_model()


class UserViewSet(djoserUserViewSet):
    '''
    用户的主要视图集
    '''
    def get_serializer_class(self):
        if self.action == "set_avatar":
            return SetUserAvatarSerializer
        return super().get_serializer_class()

    @action(["POST"], detail=False, url_name="Set Acatar", url_path="set_avatar")
    def set_avatar(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.request.user
        new_avatar = UploadImages.objects.get(id=serializer.data['avatar'])

        setattr(user, 'avatar', new_avatar)
        user.save()

        return Response(status=status.HTTP_204_NO_CONTENT,data={})

    pass
