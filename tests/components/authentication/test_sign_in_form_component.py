from unittest.mock import patch

import pytest
from django.test import RequestFactory

from authentication.components.sign_in_form import SignInFormView
from authentication.models import AppUser
from tests.conftest import USER_FIXTURE_PASSWORD


@pytest.fixture
def sign_in_form_component() -> SignInFormView:
    """
    Sign in form component fixture

    Returns
    -------
    SignInFormView
        The sign in form component instance
    """

    request_factory = RequestFactory()
    request = request_factory.post("/unicorn/message/sign-in-form")

    return SignInFormView(
        component_id="test", component_name="sign-in-form", request=request
    )


def test_sign_in_form_component_initial_state(sign_in_form_component: SignInFormView):
    """
    Tests the initial state of the sign in form component
    """

    assert sign_in_form_component.email == ""
    assert sign_in_form_component.password == ""
    assert sign_in_form_component.invalid_credentials is False


def test_sign_in_form_component_submit_empty_email_or_password(
    sign_in_form_component: SignInFormView,
):
    """
    Tests the sign in form component submit method when the email or password is empty
    and checks if nothing is returned
    """

    response = sign_in_form_component.submit()

    assert response is None


@pytest.mark.usefixtures("user")
@pytest.mark.django_db
def test_sign_in_form_component_submit_email_not_found(
    sign_in_form_component: SignInFormView,
):
    """
    Tests the sign in form component submit method when the email is not found
    and checks if the invalid credentials flag is set to True
    """

    sign_in_form_component.email = "incorrect_email"
    sign_in_form_component.password = "incorrect_password"

    sign_in_form_component.submit()

    assert sign_in_form_component.invalid_credentials is True


@pytest.mark.django_db
def test_sign_in_form_component_submit_incorrect_password(
    sign_in_form_component: SignInFormView, user: AppUser
):
    """
    Tests the sign in form component submit method when the password is incorrect
    and checks if the invalid credentials flag is set to True
    """

    sign_in_form_component.email = user.email
    sign_in_form_component.password = "incorrect_password"

    sign_in_form_component.submit()

    assert sign_in_form_component.invalid_credentials is True


@pytest.mark.django_db
def test_sign_in_form_component_submit_success(
    sign_in_form_component: SignInFormView, user: AppUser
):
    """
    Tests the sign in form component submit method when the email and password are correct
    and checks if the login function is called and the response is a redirect to the passwords page
    """

    sign_in_form_component.email = user.email
    sign_in_form_component.password = USER_FIXTURE_PASSWORD

    with patch("authentication.components.sign_in_form.login") as mock_login:
        response = sign_in_form_component.submit()

    mock_login.assert_called_once()
    assert response.status_code == 302
    assert response.url == "/passwords"
