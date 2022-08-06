import re
from turtle import title
from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# List for site menu
menu = [{'title':'O сайте', 'url_name': 'about'},
        {'title':'Категории', 'url_name': 'cathigories'},
        {'title':'Контакты', 'url_name': 'contacts'},
        {'title': 'Женщины', 'url_name':'womens'},
        {'title':'Войти', 'url_name': 'login'},
        ]


def womens(request):
    womens = Women.objects.all()
    cats = Category.objects.all()
    context = {
        'menu': menu,
        'womens': womens,
        'cats': cats,
        'cat_selected':0,
    }
    return render(request, 'womens.html', context)


def cathigories(request):
    context = {
        "menu": menu,
    }
    
    return render(request, 'cathigories.html', context)
  
    
def contacts(request):
    context = {
        "menu": menu,
    } 
    
    return render(request, 'contacts.html', context)


def about(request):
    context = {
        'menu': menu,
    }
    
    return render(request, 'about.html', context)


def post(request, post_id):
    
    return HttpResponse(f'Контент поста с id = {post_id}')


def login(request):
    context = {
        'menu': menu,
    }
    
    return render(request,'login.html', context)


def show_category(request, cat_id):
    womens = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    
    context = {
        'womens': womens,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }
    
    return render(request, 'womens.html', context)