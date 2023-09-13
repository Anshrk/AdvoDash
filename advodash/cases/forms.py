from django.forms import ModelForm, DateInput, EmailInput, TextInput, NumberInput, ChoiceField
from .models import Case



class CaseForm(ModelForm):
    class Meta:
        model = Case
        fields = '__all__' # Create a field with all the users
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Case-title', 'class': 'form-control-plaintext'}),
            'number': NumberInput(attrs={'placeholder': 'Case Number'}),
            'filling_date': DateInput(attrs={'placeholder': 'Filling-Date', 'type': 'date'}),
            'prev_date': DateInput(attrs={'type': 'date'}),
            'next_date': DateInput(attrs={'type': 'date'}),
            'party_email': EmailInput(attrs={'type': 'email'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(CaseForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control m-3'

