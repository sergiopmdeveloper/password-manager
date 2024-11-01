from django.db import models

from authentication.models import AppUser


class Password(models.Model):
    """
    Password model
    """

    user = models.ForeignKey(
        AppUser, on_delete=models.CASCADE, related_name="passwords"
    )
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    site = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        """
        String representation of the password model
        """

        return self.name

    def user_email(self):
        """
        Returns the email of the user related to the password
        """

        return self.user.email

    class Meta:
        """
        Metadata options
        """

        db_table = "passwords"
