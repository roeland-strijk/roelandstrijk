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
            'datum': forms.HiddenInput(),
            'tijd': forms.HiddenInput(),
            'incident_nr': forms.HiddenInput(),
            'incident_naam': forms.HiddenInput(),
            'locatie': forms.HiddenInput(),
        }

class Form133(forms.Form):
    incident_nr=forms.CharField(max_length=5)
    incident_naam=forms.CharField(max_length=30)
    datum=forms.DateField()
    locatie=forms.CharField(max_length=100)

def __str__(self):
        return f"{self.incident_naam} - {self.datum}"


class Form133Next(forms.Form):
    incident_nr=forms.CharField(max_length=5)
    incident_naam=forms.CharField(max_length=30, null=True, blank=True)
    locatie=forms.CharField(max_length=100, null=True, blank=True)
    datum=forms.DateField(null=True, blank=True)
    tijd=forms.CharField()
    team=forms.CharField()
    bericht=forms.CharField(max_length=100)

def __str__(self):
        return f"{self.incident_nr} - {self.tijd} - {self.team} - {self.bericht}"
