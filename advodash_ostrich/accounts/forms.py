from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import FirmUser

class FirmAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}))

class FirmUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = FirmUser
        fields = ('email', 'username', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super(FirmUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        
        return user