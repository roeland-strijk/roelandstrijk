from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.
'''
def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts_list.html', {'posts': posts})
'''
def post_page(request, id):
    # Haal de geselecteerde post op via de id
    post = Post.objects.get(id=id)
    posts = Post.objects.exclude(id=id)

    context = {
        'post': post,
        'posts': posts,
    }
    
    return render(request, 'post_page.html', context)


def posts_list(request):
    posts_1 = Post.objects.filter(kollom='a').order_by('-date')
    posts_2 = Post.objects.filter(kollom='b').order_by('-date')
    posts_3 = Post.objects.filter(kollom='c').order_by('-date')
  
    context = {
        'posts_1': posts_1,
        'posts_2': posts_2,
        'posts_3': posts_3,
    }
   
    return render(request, 'posts_list.html', context)  
  

