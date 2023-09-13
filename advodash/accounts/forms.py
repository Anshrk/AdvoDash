from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import FirmUser

class FirmUserCreationForm(UserCreationForm):
    class Meta:
        model = FirmUser
        fields = (
            "email",
            "password"
        )

class FirmUserLoginForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}))