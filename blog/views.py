from django.shortcuts import render, get_object_or_404
from .models import Blog, Category

def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs':blogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':detailblog})

def category(request, category):
    posts = Blog.objects.filter(
        categories__name__contains = category
    ).order_by(
        '-pub_date'
    )

    context = {
        'category':category,
        'posts' : posts
    }

    return render(request, 'blog/category.html', context)