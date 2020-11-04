from django.apps.config import AppConfig
from django.contrib import admin
from django.db import models
from django.db.models.query import QuerySet
from martor.widgets import AdminMartorWidget

from Campusblogs.models import Blogs, Posts , Reports


@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    search_fields = ('title',)

    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

    list_per_page = 20

    list_filter = ('created_at','activation')
    # fk_fields = ('title',)

    list_display = ['title','user','activation']

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['blog','user']



@admin.register(Reports)
class ReportsAdmin(admin.ModelAdmin):
    list_display = ['user','blog','created_at','reason','permit']
    list_filter = ['permit','created_at']
    actions = ['ReportsPermit']

    def ReportsPermit(self, request, queryset:QuerySet):
        queryset.update(permit=True)
        for Report in queryset.all():
            Report.blog.activation = False;
            Report.blog.save()
        pass;

    ReportsPermit.short_description = "许可"

