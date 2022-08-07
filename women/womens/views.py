import re
from turtle import title
from django.http import Http404, HttpResponse
from django.shortcuts import render
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


def post(request, post_id):
    return HttpResponse(f'Контент поста с id = {post_id}')


def login(request):    
    return render(request, 'login.html')


def show_category(request, cat_id):
    womens = Women.objects.filter(cat_id=cat_id)
    
    if len(womens) == 0:
        raise Http404()
    
    context = {
        'womens': womens,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }
    
    return render(request, 'womens.html', context)