from django.contrib import admin

from apps.passwords.models import Password


@admin.register(Password)
class PasswordAdmin(admin.ModelAdmin):
    """
    Password admin
    """

    list_display = ("user_email", "name", "password")
