from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


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
