from django.contrib.auth.models import AbstractUser
from django.db import models

from authentication.constants import APP_USER_EMAIL_ERRORS


class AppUser(AbstractUser):
    """
    Custom user model
    """

    email = models.EmailField(unique=True, error_messages=APP_USER_EMAIL_ERRORS)
    email_confirmed = models.BooleanField(default=False)

    def __str__(self) -> str:
        """
        String representation of the user

        Returns
        -------
        str
            The email of the user
        """

        return self.email

    class Meta:
        """
        Metadata options
        """

        db_table = "users"
        verbose_name_plural = "Users"
