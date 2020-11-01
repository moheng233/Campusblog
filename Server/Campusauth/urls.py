from django.conf.urls import include
from django.urls import path
from django.contrib.auth.views import LoginView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # path('register/', UserCreate.as_view(), name="register"),
    # path('token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]
