from django.shortcuts import render
from .models import Blog

def index(request):

    blogs = Blog.blogs.all()
    context = {
        'blogs': blogs
    }
    
    return render(request, 'index.html', context)
