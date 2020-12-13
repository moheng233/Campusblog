from django.apps.config import AppConfig
from django.contrib import admin
from django.db import models
from django.db.models.query import QuerySet
from import_export.admin import ExportActionMixin, ExportActionModelAdmin
from martor.widgets import AdminMartorWidget

from Campusblogs.models import Blogs, Classify, Posts, Reports, UploadImages

from .resources import BlogsResources


@admin.register(UploadImages)
class UploadImagesAdmin(admin.ModelAdmin):
    search_fields = ('user',)
    list_display = ['id','user','file']

@admin.register(Blogs)
class BlogsAdmin(ExportActionMixin,admin.ModelAdmin):
    resource_class = BlogsResources
    search_fields = ('title',)

    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

    list_per_page = 20

    list_filter = ('created_at','classify','activation')
    # fk_fields = ('title',)

    list_display = ['title','user','classify','activation']

# @admin.register(Posts)
# class PostsAdmin(admin.ModelAdmin):
#     list_display = ['blog','user']

@admin.register(Reports)
class ReportsAdmin(admin.ModelAdmin):
    list_display = ['user','informants','created_at','reason','permit']
    list_filter = ['permit','created_at']
    actions = ['ReportsPermit']

    def ReportsPermit(self, request, queryset:QuerySet):
        queryset.update(permit=True)
        for Report in queryset.all():
            Report.informants.is_active = False;
            Report.informants.save()
        pass;

    ReportsPermit.short_description = "许可"

@admin.register(Classify)
class ClassifyAdmin(admin.ModelAdmin):
    pass;
