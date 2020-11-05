from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import BooleanField, CharField, TextField
from django.db.models.fields.related import ForeignKey

# Create your models here.

class UploadImages(models.Model):
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,verbose_name="作者",related_name="uploadimage")
    # blog = ForeignKey(Blogs, on_delete=models.CASCADE, verbose_name="博客", related_name="uploadimage")
    file = models.ImageField('图片',upload_to='static/upload')

    def __str__(self) -> str:
        return str(self.file)

    class Meta:
        verbose_name = '上传图片'
        verbose_name_plural = verbose_name
    
    pass

class Blogs(models.Model):
    title = CharField('标题',max_length=100)
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,verbose_name="作者",related_name="blogs")
    subtitle = CharField('二级标题',max_length=200,default='')
    content = TextField('内容',default='')

    created_at = models.DateTimeField(auto_now_add=True, null=False,verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, null=False,verbose_name="修改时间")

    subimage = ForeignKey(UploadImages,on_delete=models.CASCADE,verbose_name="头图",related_name="subimage")

    activation = models.BooleanField('激活',default=True)

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

class Reports(models.Model):
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="举报人", related_name="informant");
    blog = ForeignKey(Blogs, on_delete=models.CASCADE, verbose_name="博客", related_name="blog")

    created_at = models.DateTimeField(auto_now_add=True, null=False,verbose_name="创建时间")

    reason = TextField('原因',default="")

    permit = BooleanField("许可",default=False)

    class Meta:
        verbose_name = "举报"
        verbose_name_plural = "举报"