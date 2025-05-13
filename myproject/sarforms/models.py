from django.db import models

# Create your models here.
class Form133(models.Model):
    incident_nr = models.IntegerField(null=True, blank=True)
    #incident_nr=models.CharField(max_length=5, null=True, blank=True)
    incident_naam=models.CharField(max_length=30)
    datum=models.DateField()
    locatie=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.incident_naam} - {self.datum}"



class Form133Next(models.Model):
    incident_nr=models.CharField(max_length=5)
    incident_naam=models.CharField(max_length=30, null=True, blank=True)
    locatie=models.CharField(max_length=100, null=True, blank=True)
    datum=models.DateField(null=True, blank=True)
    tijd=models.CharField()
    team=models.CharField()
    bericht=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.incident_nr} - {self.tijd} - {self.team} - {self.bericht}"