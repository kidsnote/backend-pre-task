from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    profile_photo = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=128)
    company_name = models.CharField(max_length=128, blank=True, null=True)
    company_position = models.CharField(max_length=128, blank=True, null=True)
    memo = models.TextField(blank=True, null=True)


class Label(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='labels')
    name = models.CharField(max_length=128)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='name')
        ]

    def __str__(self):
        return self.name


class AbstractLabeledData(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.SET_NULL, null=True, blank=True, default=None)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk:
            if self.contact.user != self.label.user:
                raise ValidationError('Contact and Label owner have to be same')
        super().save(*args, **kwargs)


class ContactEmail(AbstractLabeledData):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='emails')
    email = models.EmailField()


class ContactPhoneNumber(AbstractLabeledData):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='phone_numbers')
    phone_number = PhoneNumberField()


class ContactAddress(AbstractLabeledData):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='addresses')
    address = models.TextField()


class ContactImportantDate(AbstractLabeledData):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='important_dates')
    important_date = models.DateField()


class ContactWebsite(AbstractLabeledData):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='websites')
    website = models.URLField()
