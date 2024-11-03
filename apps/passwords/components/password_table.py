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

        self.load_passwords()

    def delete_password(self, password_id: int) -> None:
        """
        Deletes a password
        """

        password = Password.objects.get(id=password_id)
        password.delete()

        self.load_passwords()

    def load_passwords(self) -> None:
        """
        Loads passwords
        """

        user: AppUser = self.request.user

        self.user_passwords = user.passwords.all()
