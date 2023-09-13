from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import FirmUser

class FirmUserCreationForm(UserCreationForm):
    class Meta:
        model = FirmUser
        fields = '__all__'