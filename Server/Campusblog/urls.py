"""Campusblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from Campusblogs import views
from django.conf.urls import url
from django.contrib import admin, auth
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from constance import config

router = routers.DefaultRouter()
router.register(r'blogs', views.BlogViewSet)
router.register(r'classify',views.ClassifyViewSet)
router.register(r'uploadimage', views.UploadImagesViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'reports', views.ReportsViewSet)

admin.site.site_header = getattr(config,'site_name')

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('Campusauth.urls')),
    path('martor/', include('martor.urls')),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
]
