from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from datetime import datetime
from .models import Blog
# Create your views here.

def index(request):
    blogs = Blog.objects.all()
    context = {
    'blogs': blogs
    }
    return render(request, 'index.html', context)

def my_posts(request):
    my_posts = Blog.objects.filter(author=request.user.username)
    context = {
    'my_posts': my_posts
    }
    return render(request, 'my_posts.html', context)


def post_detail(request, post_id):
    blog = Blog.objects.get(id=post_id)
    context = {
        'post_id': post_id,
        'blog': blog
    }
    return render(request, 'post_detail.html', context)

def delete_post(request, post_id):
    blog = Blog.objects.get(id=post_id)
    if request.user.username == blog.author:
        blog.delete()
        return redirect('index')
    else:
        messages.error(request, 'You can only delete posts published by you')
        return redirect('post_detail', post_id)

def add_post(request):

    if request.method == 'POST':
        title = request.POST['title']
        author = request.user.username
        content = request.POST['content']
        created_date = datetime.now()

        new_post = Blog.objects.create(title=title, author=author, content=content, created_date=created_date)
        return redirect('index')

    else:
        return render(request, 'add_post.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password == password_confirm:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'email already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                # messages.success(request, 'User created successfully')
                return redirect('login')
        else:
            messages.error(request, 'passwords do not match')
            return redirect('register')

    else:
        return render(request, 'register.html')
