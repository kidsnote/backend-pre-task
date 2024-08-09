from rest_framework.filters import OrderingFilter
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.contact.models import Contact, Label

from api.v1.contact.serializers import ContactSerializer, ContactDetailSerializer, LabelSerializer


class ContactViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin):
    model = Contact
    serializer_class = ContactDetailSerializer
    queryset = Contact.objects.all()
    filter_backends = (OrderingFilter, )
    ordering_fields = ['name', 'emails__email', 'phone_numbers__phone_number']
    ordering = []

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            user=self.request.user
        )
        queryset = queryset.prefetch_related('emails')
        queryset = queryset.prefetch_related('emails__label')
        queryset = queryset.prefetch_related('phone_numbers')
        queryset = queryset.prefetch_related('phone_numbers__label')
        queryset = queryset.prefetch_related('addresses')
        queryset = queryset.prefetch_related('addresses__label')
        queryset = queryset.prefetch_related('important_dates')
        queryset = queryset.prefetch_related('important_dates__label')
        queryset = queryset.prefetch_related('websites')
        queryset = queryset.prefetch_related('websites__label')
        return queryset

    def get_serializer_class(self):
        if self.request.method == 'GET' and self.action == 'list':
            return ContactSerializer
        return super().get_serializer_class()


class LabelViewSet(GenericViewSet, CreateModelMixin, ListModelMixin):
    model = Label
    serializer_class = LabelSerializer

    def get_queryset(self):
        return Label.objects.filter(user=self.request.user)
