from django.db import models
from django.core.validators import RegexValidator
from ..users.models import User


class Label(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"label: {self.name}"

    class Meta:
        verbose_name = "Label"


class Contact(models.Model):
    contact_number_regex = RegexValidator(
        regex=r"^[0-9-]+$", message="Contact number must only contain digits and '-'."
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contacts")
    profile_image = models.URLField(blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    contact_number = models.CharField(
        max_length=30, validators=[contact_number_regex], blank=True
    )
    company = models.CharField(max_length=100, blank=True)
    job_title = models.CharField(max_length=100, blank=True)
    memo = models.TextField(blank=True)
    labels = models.ManyToManyField(Label, related_name="contacts", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # 기타 항목
    address = models.TextField(blank=True)
    birthday = models.DateField(null=True, blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return f"{self.user.email}'s contact: {self.name}"

    class Meta:
        verbose_name = "Contact"
