import re
from turtle import title
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *

# List for site menu



def womens(request):
    womens = Women.objects.all()
    context = {
        'womens': womens,
        'cat_selected':0,
    }
    return render(request, 'womens.html', context)


def cathigories(request):
    return render(request, 'cathigories.html')
  
    
def contacts(request):   
    return render(request, 'contacts.html')


def about(request):
    return render(request, 'about.html')


def show_post(request, slug_id):
    post = get_object_or_404(Women, slug=slug_id)
    
    context = {
        "post": post,
        "title": post.title,
        "cat_selected":post.slug,
    }
    
    return render(request, 'post.html', context)


def login(request):    
    return render(request, 'login.html')


def show_category(request, slug_id):
    cat = Category.objects.get(slug=slug_id)
    womens = Women.objects.filter(cat_id=cat.pk)
    
    if len(womens) == 0:
        raise Http404()
    
    context = {
        'womens': womens,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat.pk,
    }
    
    return render(request, 'womens.html', context)