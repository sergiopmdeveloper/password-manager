from django.urls import path

from apps.passwords import views

urlpatterns = [
    path("", views.PasswordsView.as_view(), name="passwords"),
]
