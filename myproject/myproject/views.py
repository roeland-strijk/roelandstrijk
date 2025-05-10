#from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    #return HttpResponse("Hello World! I'm Home.")
    return render(request, 'index.html')


#def radiolog(request):
    # return HttpResponse("My About page.")
   # return render(request, 'radio_log.html')