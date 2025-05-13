from django.shortcuts import render
from .models import Form133, Form133Next
from django.db.models import Max


def radio_log(request):
    if request.method=="POST":
        post=Form133()
        post.incident_nr=request.POST['incident_nr']
        post.incident_naam=request.POST['incident_naam']
        post.datum=request.POST['datum']
        post.locatie=request.POST['locatie']
        post.save()


    laatste = Form133.objects.last()
    volgend_incident_nr = (Form133.objects.aggregate(Max('incident_nr'))['incident_nr__max'] or 0) + 1

    context = {
        'laatste': laatste,
        'volgend_incident_nr': volgend_incident_nr,
    }
    return render(request, 'radio_register.html', context)

     # bij GET ook de laatste meegeven
#laatste = Form133.objects.last()
#return render(request, 'radio_register.html', {'laatste': laatste})

    

def radio_log_combined(request):
    if request.method == "POST":
        post = Form133Next()
        post.incident_nr = request.POST['incident_nr']
        post.incident_naam= request.POST['incident_naam']
        post.locatie=request.POST['locatie']
        post.datum=request.POST['datum']
        post.tijd = request.POST['tijd']
        post.team = request.POST['team']
        post.bericht = request.POST['bericht']
        post.save()



    max_incident_nr = Form133.objects.aggregate(Max('incident_nr'))['incident_nr__max']
    logs = Form133Next.objects.filter(incident_nr=max_incident_nr)

   
    #logs = Form133Next.objects.all().order_by('-incident_nr')
    #logs = Form133Next.objects.all()
    incident = Form133.objects.all()
    laatste = Form133.objects.last()
    context = {

        'form133next': logs,
        'form133': incident,
        'laatste': laatste,
    }

    return render(request, 'radio_log_combined.html', context)