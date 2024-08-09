from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.contact.views import ContactViewSet, LabelViewSet

router = DefaultRouter()
router.register('contact', ContactViewSet, basename='contact')
router.register('label', LabelViewSet, basename='label')

urlpatterns = [
    path('', include(router.urls)),
]
