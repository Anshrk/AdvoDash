from django.forms import ModelForm, DateInput, EmailInput
from .models import Case



class CaseForm(ModelForm):
    class Meta:
        model = Case
        fields = '__all__' # Create a field with all the users
        widgets = {
            'filling_date': DateInput(attrs={'type': 'date'}),
            'prev_date': DateInput(attrs={'type': 'date'}),
            'next_date': DateInput(attrs={'type': 'date'}),
            'party_email': EmailInput(attrs={'type': 'email'}),
        }
    

