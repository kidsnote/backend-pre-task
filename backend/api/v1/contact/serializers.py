from django.db.transaction import atomic
from rest_framework import serializers

from apps.contact.models import (
    Contact, ContactEmail, ContactPhoneNumber, ContactAddress, ContactImportantDate,
    ContactWebsite, Label, )


class LabelField(serializers.CharField):
    def to_representation(self, value):
        return value.name

    def to_internal_value(self, data):
        return Label.objects.get(name=data, user=self.context['request'].user)


class ContactEmailSerializer(serializers.ModelSerializer):
    label = LabelField()

    class Meta:
        model = ContactEmail
        fields = (
            'email',
            'label'
        )


class ContactPhoneNumberSerializer(serializers.ModelSerializer):
    label = LabelField()

    class Meta:
        model = ContactPhoneNumber
        fields = (
            'phone_number',
            'label'
        )


class ContactAddressSerializer(serializers.ModelSerializer):
    label = LabelField()

    class Meta:
        model = ContactAddress
        fields = (
            'address',
            'label'
        )


class ContactImportantDateSerializer(serializers.ModelSerializer):
    label = LabelField()

    class Meta:
        model = ContactImportantDate
        fields = (
            'important_date',
            'label'
        )


class ContactWebSiteSerializer(serializers.ModelSerializer):
    label = LabelField()

    class Meta:
        model = ContactWebsite
        fields = (
            'website',
            'label'
        )


class ContactSerializer(serializers.ModelSerializer):
    emails = ContactEmailSerializer(many=True)
    phone_numbers = ContactPhoneNumberSerializer(many=True)

    class Meta:
        model = Contact
        fields = (
            'id',
            'profile_photo',
            'name',
            'emails',
            'phone_numbers',
            'company_name',
            'company_position',
        )


class ContactDetailSerializer(serializers.ModelSerializer):
    emails = ContactEmailSerializer(many=True)
    phone_numbers = ContactPhoneNumberSerializer(many=True)
    addresses = ContactAddressSerializer(many=True)
    important_dates = ContactImportantDateSerializer(many=True)
    websites = ContactWebSiteSerializer(many=True)

    class Meta:
        model = Contact
        fields = (
            'id',
            'profile_photo',
            'name',
            'emails',
            'phone_numbers',
            'company_name',
            'company_position',
            'memo',
            'addresses',
            'important_dates',
            'websites',
        )

    @atomic
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        emails = validated_data.pop('emails', [])
        phone_numbers = validated_data.pop('phone_numbers', [])
        addresses = validated_data.pop('addresses', [])
        important_dates = validated_data.pop('important_dates', [])
        websites = validated_data.pop('websites', [])
        contact = super().create(validated_data)
        for email in emails:
            ContactEmail.objects.create(contact=contact, **email)
        for phone_number in phone_numbers:
            ContactPhoneNumber.objects.create(contact=contact, **phone_number)
        for address in addresses:
            ContactAddress.objects.create(contact=contact, **address)
        for important_date in important_dates:
            ContactImportantDate.objects.create(contact=contact, **important_date)
        for website in websites:
            ContactWebsite.objects.create(contact=contact, **website)
        return contact


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ('name', )

    @atomic
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
