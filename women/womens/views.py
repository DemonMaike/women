from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.

def womens(request):
    womens = Women.objects.all()
    context = {
        'womens': womens,
    }
    return render(request, 'index.html', context)