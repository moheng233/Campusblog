from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):

    avatar = models.ImageField('头像',upload_to='static/avatar',default="/static/avatar/avatar.jpg")

    pass
