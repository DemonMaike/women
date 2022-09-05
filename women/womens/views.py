from multiprocessing import context
import re
from tkinter import Menu
from turtle import title
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from .utils import DataMixin
from django.contrib.auth.mixins import LoginRequiredMixin 

# List for site menu


class WomenHome(DataMixin, ListView):
    model = Women
    template_name = 'womens.html'
    context_object_name = 'womens'
    
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Главная страница')
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return Women.objects.filter(is_published=True) 

#def womens(request):
#    womens = Women.objects.all().order_by('-time_create')
#
#    context = {
#        'womens': womens,
#        'cat_selected':0,
#    }
#    return render(request, 'womens.html', context)


class AddPost(LoginRequiredMixin, DataMixin, CreateView):
    form_class = CreateWomen
    template_name = 'add_post.html'
    success_url = reverse_lazy('womens')
    login_url = reverse_lazy('womens')
    raise_exception = True
    
    def get_context_data(self, * ,objcets_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Добавление статьи')
        return dict(list(context.items()) + list(c_def.items()))
    
    
    
#def add_post(request):
#    if request.method == "POST":
#        form = CreateWomen(request.POST, request.FILES)
#        if form.is_valid():
#            try:
#                form.save()
#                return redirect ('womens')
#            except:
#                form.add_error(None,'Ошибка добавления поста')
#    else:
#        form = CreateWomen()
#    
#    context = {
#        'title': 'Добавление статьи',
#        'form': form
#    }
#    return render(request, 'add_post.html', context)
  
    
def contacts(request):   
    return render(request, 'contacts.html')


def about(request):
    return render(request, 'about.html')


class Show_post(DataMixin, DetailView):
    model = Women
    template_name = 'post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    
    def get_context_data(self, *, object_list = None, **kwargs):
        cotext = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = context['post'])
        return dict(list(context.items()) + list(c_def.items()))
    

#def show_post(request, slug_id):
#    post = get_object_or_404(Women, slug=slug_id)
#    
#    context = {
#        "post": post,
#        "title": post.title,
#        "cat_selected":post.slug,
#    }
#    
#    return render(request, 'post.html', context)


def login(request):    
    return render(request, 'login.html')


class WomenCategory(DataMixin, ListView):
    model = Women
    template_name = 'womens.html'
    context_object_name ='womens'
    allow_empty = False
    
    def get_context_data(self, *,object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Категория - " + str(context['womens'][0].cat)
        context['cat_selected'] = context['womens'][0].cat_id
        
        c_def = self.get_user_context(title = "Категория - " + str(context['womens'][0].cat), cat_selected = context['womens'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['slug_id'],is_published = True)

#def show_category(request, slug_id):
#    cat = Category.objects.get(slug=slug_id)
#    womens = Women.objects.filter(cat_id=cat.pk)
#    
#    if len(womens) == 0:
#        raise Http404()
#    
#    context = {
#        'womens': womens,
#        'title': 'Отображение по рубрикам',
#        'cat_selected': cat.pk,
#    }
#    
#    return render(request, 'womens.html', context)