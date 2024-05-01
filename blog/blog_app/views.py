from django.shortcuts import render, redirect
from .models import Blog
# Create your views here.

def index(request):
    blogs = Blog.objects.all()
    context = {
    'blogs': blogs
    }

    return render(request, 'index.html', context)

def post_detail(request, post_id):
    blog = Blog.objects.get(id=post_id)
    context = {
        'post_id': post_id,
        'blog': blog
    }
    return render(request, 'post_detail.html', context)
