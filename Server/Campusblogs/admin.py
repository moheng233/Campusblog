from django.apps.config import AppConfig
from django.contrib import admin
from django.db import models
from martor.widgets import AdminMartorWidget

from Campusblogs.models import Blogs, Posts


@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    search_fields = ('title',)

    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

    list_per_page = 20

    list_filter = ('created_at',)
    # fk_fields = ('title',)

    list_display = ['title','user']

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['blog','user']

