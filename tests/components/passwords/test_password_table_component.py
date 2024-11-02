import pytest
from django.test import RequestFactory

from apps.passwords.components.password_table import PasswordTableView
from authentication.models import AppUser


@pytest.fixture
def password_table_component(user: AppUser) -> PasswordTableView:
    """
    Password table component fixture

    Parameters
    ----------
    user : AppUser
        The user to include in the request

    Returns
    -------
    PasswordTableView
        The password table component instance
    """

    request_factory = RequestFactory()
    request = request_factory.post("/unicorn/message/password-table")
    request.user = user

    return PasswordTableView(
        component_id="test", component_name="password-table", request=request
    )


@pytest.mark.usefixtures("passwords")
@pytest.mark.django_db
def test_password_table_component_initial_state(
    password_table_component: PasswordTableView, user: AppUser
):
    """
    Tests the initial state of the password table component
    """

    password_table_component.mount()

    assert list(password_table_component.user_passwords) == list(user.passwords.all())