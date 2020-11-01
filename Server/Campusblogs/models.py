from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import CharField, TextField
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Blogs(models.Model):
    title = CharField('标题',max_length=100)
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,verbose_name="作者",related_name="blogs")
    subtitle = CharField('二级标题',max_length=200,default='')
    content = TextField('内容',default='')

    created_at = models.DateTimeField(auto_now_add=True, null=False,verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, null=False,verbose_name="修改时间")

    subimage = models.ImageField('头图',upload_to='static/blogs')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    pass

class Posts(models.Model):
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="回复者", related_name="posts")
    blog = ForeignKey(Blogs, on_delete=models.CASCADE, verbose_name="博客", related_name="posts")

    content = TextField('内容',default="")

    created_at = models.DateTimeField(auto_now_add=True, null=False,verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, null=False,verbose_name="修改时间")

    class Meta:
        verbose_name = '回复'
        verbose_name_plural = verbose_name
