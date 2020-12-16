from Campusblogs.models import UploadImages
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    '''
    从Django自带的AbstractUser模型扩展的用户模型
    '''

    avatar = models.ForeignKey(UploadImages,on_delete=models.CASCADE,verbose_name="头像",related_name="avatar",null=True)

    pass
