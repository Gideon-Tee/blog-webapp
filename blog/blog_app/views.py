from django.shortcuts import render, redirect
from .models import Blog
# Create your views here.

def index(request):
    blogs = Blog.objects.all()
    context = {
    'blogs': blogs
    }

    return render(request, 'index.html', context)
