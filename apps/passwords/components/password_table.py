from django.db.models.query import QuerySet
from django_unicorn.components import UnicornView

from apps.passwords.models import Password


class PasswordTableView(UnicornView):
    """
    Password table component
    """

    user_passwords: QuerySet[Password]

    def mount(self) -> None:
        """
        Mounts the component
        """

        self.user_passwords = self.request.user.passwords.all()
