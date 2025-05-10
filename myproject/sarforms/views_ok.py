from django.shortcuts import render
from .models import Form133, Form133Next
#from .forms import Form133, Form133Next

def radio_log(request):
    if request.method=="POST":
        post=Form133()
        post.incident_nr=request.POST['incident_nr']
        post.incident_naam=request.POST['incident_naam']
        post.datum=request.POST['datum']
        post.locatie=request.POST['locatie']
        post.save()
        return render(request, 'radio_register.html')
    else:
        return render(request, 'radio_register.html')
    
def radio_lognext(request):
    if request.method=="POST":
        post=Form133Next()
        post.incident_nr=request.POST['incident_nr']
        post.tijd=request.POST['tijd']
        post.team=request.POST['team']
        post.bericht=request.POST['bericht']
        post.save()
        return render(request, 'radio_log.html')
    else:
        return render(request, 'radio_log.html')
    



def radio_loglist(request):
    logs = Form133Next.objects.all()
    context = {
        'form133next': logs,
    }
    return render(request, 'radio_loglist.html', context)