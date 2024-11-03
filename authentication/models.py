from typing import TYPE_CHECKING

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import QuerySet

if TYPE_CHECKING:
    from apps.passwords.models import Password


class AppUser(AbstractUser):
    """
    Custom user model
    """

    email = models.EmailField(unique=True, error_messages={"unique": "Email already exists."})
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

    @property
    def passwords(self) -> QuerySet["Password"]:
        """
        User passwords queryset facade

        Returns
        -------
        QuerySet[Password]
            The user passwords queryset
        """

        return self.passwords

    class Meta:
        """
        Metadata options
        """

        db_table = "users"
        verbose_name_plural = "Users"
