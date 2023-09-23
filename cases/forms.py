
from django.forms import ModelForm, DateInput, EmailInput, TextInput, NumberInput, ChoiceField
from .models import Cases

class CaseForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(CaseForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Cases
        fields = '__all__' # Create a field with all the users
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Case-title'}),
            'number': NumberInput(attrs={'placeholder': 'Case Number'}),
            'filling_date': DateInput(attrs={'placeholder': 'Filling-Date', 'type': 'date'}),
            'prev_date': DateInput(attrs={'type': 'date'}),
            'next_date': DateInput(attrs={'type': 'date'}),
            'party_email': EmailInput(attrs={'type': 'email'}),
        }
        

