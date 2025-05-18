from django.shortcuts import render, redirect
from django.db.models import Max
from .models import Form133, Form133Next
from .forms import Form133Form, Form133NextForm

def radio_log(request):
    laatste = Form133.objects.last()
    volgend_incident_nr = (Form133.objects.aggregate(Max('incident_nr'))['incident_nr__max'] or 0) + 1

    if request.method == "POST":
        form = Form133Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logs')  # Pas aan naar jouw URL naam

    else:
        form = Form133Form(initial={'incident_nr': volgend_incident_nr})

    context = {
        'form': form,
        'laatste': laatste,
        'volgend_incident_nr': volgend_incident_nr,
    }
    return render(request, 'radio_register.html', context)

# dit is het formulier voor de radio log pagina.
def radio_log_combined(request):
    if request.method == "POST":
        form = Form133NextForm(request.POST)
        if form.is_valid():
            form.save()

    max_incident_nr = Form133.objects.aggregate(Max('incident_nr'))['incident_nr__max']
    logs = Form133Next.objects.filter(incident_nr=max_incident_nr).order_by('-datum', '-tijd')

    incidenten = Form133.objects.all()
    laatste = Form133.objects.last()
    form = Form133NextForm(initial={'incident_nr': max_incident_nr})

    context = {
        'form': form,
        'form133next': logs,
        'form133': incidenten,
        'laatste': laatste,
    }

    return render(request, 'radio_log_combined.html', context)


