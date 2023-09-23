from typing import Any
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http.request import HttpRequest

class CustomBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        ...