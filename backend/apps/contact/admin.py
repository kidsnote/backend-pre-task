from django.contrib import admin

from .models import Contact, Label


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
