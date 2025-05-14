from django import forms


class Form133(forms.Form):
    incident_nr=forms.IntegerField(null=True, blank=True)
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