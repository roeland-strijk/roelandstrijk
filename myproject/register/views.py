from django.shortcuts import render
from .models import register

def registration(request):
    if request.method=="POST":
        post=register()
        post.name=request.POST['name']
        post.email=request.POST['email']
        post.phone=request.POST['phone']
        post.address=request.POST['address']
        post.save()
        return render(request, 'registration.html')
    else:
        return render(request, 'registration.html')