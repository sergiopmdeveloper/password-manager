from typing import Optional

from django import forms
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django_unicorn.components import UnicornView

from authentication.models import AppUser


class SignInFormForm(forms.Form):
    """
    Sign in form component form
    """

    email = forms.CharField(required=True, error_messages={"required": "Email is required."})
    password = forms.CharField(required=True, error_messages={"required": "Password is required."})


class SignInFormView(UnicornView):
    """
    Sign in form component
    """

    form_class = SignInFormForm

    email = ""
    password = ""
    invalid_credentials = False

    def submit(self) -> Optional[HttpResponseRedirect]:
        """
        Submits the form

        Returns
        -------
        Optional[HttpResponseRedirect]
            Nothing if there are validation errors
            or a redirect to the passwords page
        """

        self.validate()

        if not self.is_valid():
            if self.invalid_credentials:
                self.invalid_credentials = False

            return

        user = AppUser.objects.filter(email=self.email).first()

        if not user:
            self.invalid_credentials = True
            return

        if not user.check_password(self.password):
            self.invalid_credentials = True
            return

        login(self.request, user)

        return redirect("/passwords")
