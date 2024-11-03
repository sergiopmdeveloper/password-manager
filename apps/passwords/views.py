from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class PasswordsView(View):
    """
    Passwords view
    """

    def get(self, request: WSGIRequest) -> HttpResponse:
        """
        Renders the passwords page

        Parameters
        ----------
        request : WSGIRequest
            The request object

        Returns
        -------
        HttpResponse
            The rendered passwords page
        """

        return render(request, "passwords/index.html")
