from django_unicorn.components import UnicornView

from apps.passwords.models import Password


class PasswordRowView(UnicornView):
    """
    Password row component
    """

    password: Password
    displayed_modal = False

    def display_modal(self) -> None:
        """
        Displays a modal
        """

        self.displayed_modal = True

    def hide_modal(self) -> None:
        """
        Hides the modal
        """

        self.displayed_modal = False
