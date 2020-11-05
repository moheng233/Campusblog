from django.conf.urls import include
from django.contrib.auth.views import LoginView
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet

router = DefaultRouter()
router.register("users", UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls.jwt'))
]
