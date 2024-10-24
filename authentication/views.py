import json

from django.contrib.auth import login
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

from authentication.models import AppUser


class SignInView(View):
    """
    Sign in view
    """

    def get(self, request: WSGIRequest) -> HttpResponse:
        """
        Renders the sign in page

        Parameters
        ----------
        request : WSGIRequest
            The request object

        Returns
        -------
        HttpResponse
            The rendered sign in page
        """

        return render(request, "authentication/sign-in.html")

    def post(self, request: WSGIRequest) -> JsonResponse | HttpResponse:
        """
        Signs in the user

        Parameters
        ----------
        request : WSGIRequest
            The request object

        Returns
        -------
        JsonResponse | HttpResponse
            A JSON response with errors if there are any
            or an HTTP response with status 200
        """

        email = json.loads(request.body)["email"]
        password = json.loads(request.body)["password"]

        errors = {}

        if not email:
            errors["email"] = "Email is required."

        if not password:
            errors["password"] = "Password is required."

        if errors:
            return JsonResponse(errors, status=400)

        user = AppUser.objects.filter(email=email).first()

        if not user or not user.check_password(password):
            errors["invalid_credentials"] = "Incorrect email or password."
            return JsonResponse(errors, status=400)

        login(request, user)

        return HttpResponse(status=200)
