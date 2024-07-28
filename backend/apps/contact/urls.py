from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LabelViewSet, ContactViewSet

router = DefaultRouter()
router.register(r"", ContactViewSet)
router.register(r"labels", LabelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
