from django import forms
from .models import Form133, Form133Next

class Form133Form(forms.ModelForm):
    class Meta:
        model = Form133
        fields = ['incident_nr', 'incident_naam', 'datum', 'locatie']
        widgets = {
            'datum': forms.DateInput(attrs={'type': 'date'}),
        }

class Form133NextForm(forms.ModelForm):
    class Meta:
        model = Form133Next
        fields = ['incident_nr', 'incident_naam', 'locatie', 'datum', 'tijd', 'team', 'bericht']
        widgets = {
            'datum': forms.DateInput(attrs={'type': 'date'}),
            'tijd': forms.TimeInput(attrs={'type': 'time'}),
        }