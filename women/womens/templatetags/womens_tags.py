from django import template

from womens.models import *

register = template.Library()

menu = [{'title':'O сайте', 'url_name': 'about'},
        {'title':'Категории', 'url_name': 'cathigories'},
        {'title':'Контакты', 'url_name': 'contacts'},
        {'title': 'Женщины', 'url_name':'womens'},
        {'title':'Войти', 'url_name': 'login'},
        ]

@register.simple_tag(name='get_cat')
def get_category(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)
    
@register.inclusion_tag('list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    
    return {'cats': cats, 'cat_selected': cat_selected}

@register.inclusion_tag('list_menu.html')
def show_menu():
    return {'menu': menu}
