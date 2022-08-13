from django import forms
from .models import *


class CreateWomen(forms.Form):
    title = forms.CharField(max_length=100, label='Заголовок')
    slug = forms.SlugField(max_length=100, label='Ссылка')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Контент')
    is_published = forms.BooleanField(label='Опубликовано')
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label="Категория не выбрана")
    

    