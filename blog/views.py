from django.shortcuts import render
from .models import Blog

def index(request):
    blogs = Blog.blogs.all()
    context = {
        'blogs': blogs
    }
    
    return render(request, 'index.html', context)

def post_detail(request, slug):
    blog = Blog.blogs.get(slug=slug)

    context = {
        'blog': blog,
    }
    
    return render(request, 'post_detail.html', context)
