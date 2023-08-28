from django.urls import path
from.views import index, home, contact, register, user

urlpatterns = [
    path("", index, name="acceuil"),
    path("home/", home),
    path("contact/", contact),
    path("register/", register),
    path("user/", user)
]
