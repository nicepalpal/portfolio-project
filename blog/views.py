from django.shortcuts import render, get_object_or_404

from .models import Blog

def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs': blogs})

def detail(request, blog_id):
    #uses above import of get object 404 to grab object or get_object_or_404
    #Pk is primary key, takes blog_id from urls.py and checks DB for all blogs)
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render (request, 'blog/detail.html', {'blog': detailblog})
