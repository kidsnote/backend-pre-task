from rest_framework import serializers
from .models import Label, Contact


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class ContactListSerializer(serializers.ModelSerializer):
    labels = LabelSerializer(many=True, read_only=True)
    company_with_job_title = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = [
            "id",
            "profile_image",
            "name",
            "email",
            "contact_number",
            "company_with_job_title",
            "labels",
        ]

    def get_company_with_job_title(self, obj):
        if obj.company and obj.job_title:
            return f"{obj.company} ({obj.job_title})"
        elif obj.company:
            return obj.company
        elif obj.job_title:
            return obj.job_title
        return ""
