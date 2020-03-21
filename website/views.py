from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from website.models import Page, Post, Work


def home_view(request):
    posts = Post.objects.all().order_by('-date_published')[:2]
    works = Work.objects.all().order_by('-date_published')[:3]

    context = {
        'posts': posts,
        'works': works
    }

    return render(request, 'website/home.html', context)


def blog_view(request):
    posts = Post.objects.all().order_by('-date_published')

    context = {
        'posts': posts
    }

    return render(request, 'website/blog.html', context)


def works_view(request):
    works = Work.objects.all().order_by('-date_published')

    context = {
        'works': works
    }

    return render(request, 'website/works.html', context)


def page_view(request, permalink=''):
    page = get_object_or_404(Page, permalink=permalink)

    context = {
        'page': page
    }

    return render(request, 'website/page.html', context)
