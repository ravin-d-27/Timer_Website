from django import forms
from .models import Timer

class TimerForm(forms.ModelForm):
    # Add the is_captain field to the form
    is_captain = forms.BooleanField(label='Are you a Captain?', required=False)

    class Meta:
        model = Timer
        fields = ['name', 'is_captain']
