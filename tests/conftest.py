import pytest
from django.db.models.query import QuerySet

from apps.passwords.models import Password
from authentication.models import AppUser

USER_FIXTURE_PASSWORD = "password12345"


@pytest.fixture
def user() -> AppUser:
    """
    User fixture

    Returns
    -------
    AppUser
        The user instance
    """

    return AppUser.objects.create_user(
        username="test", email="test@email.com", password=USER_FIXTURE_PASSWORD
    )


@pytest.fixture
def passwords(user: AppUser) -> QuerySet[Password]:
    """
    Passwords fixture

    Parameters
    ----------
    user : AppUser
        The user to create the passwords for

    Returns
    -------
    QuerySet[Password]
        The password instances
    """

    passwords = [
        {
            "name": "Test password 1",
            "password": "password12345",
            "username": "test",
            "email": "test@email.com",
            "site": "https://www.testsite.com",
        },
        {
            "name": "Test password 2",
            "password": "password12345",
            "username": "test",
            "email": "test@email.com",
            "site": "https://www.testsite.com",
        },
    ]

    for password in passwords:
        Password.objects.create(user=user, **password)

    return user.passwords.all()
