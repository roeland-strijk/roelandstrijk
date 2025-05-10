from django import forms


class Form133(forms.Form):
    incident_nr=forms.CharField(max_length=5)
    incident_naam=forms.CharField(max_length=30)
    datum=forms.DateField()
    locatie=forms.CharField(max_length=100)


class Form133Next(forms.Form):
    incident_nr=forms.CharField(max_length=5)
    tijd=forms.CharField()
    team=forms.CharField()
    bericht=forms.CharField(max_length=100)