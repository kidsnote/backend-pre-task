from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenVerifyView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r"", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("token/obtain/", TokenObtainPairView.as_view(), name="jwt_token_obtain"),
    path("token/refresh/", TokenRefreshView.as_view(), name="jwt_token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="jwt_token_verify"),
]
