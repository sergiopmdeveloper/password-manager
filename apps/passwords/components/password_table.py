from django.db.models.query import QuerySet
from django_unicorn.components import UnicornView

from apps.passwords.models import Password
from authentication.models import AppUser


class PasswordTableView(UnicornView):
    """
    Password table component
    """

    user_passwords: QuerySet[Password]

    def mount(self) -> None:
        """
        Mounts the component
        """

        user: AppUser = self.request.user

        self.user_passwords = user.passwords.all()
