from django.urls import path
from .views import *

urlpatterns = [
    path('', womens, name = 'womens'),
    path('about/', about, name = 'about'),
    path('cathigories/', cathigories, name = 'cathigories'),
    path('contacts/', contacts, name = 'contacts'),
    path('post/<slug:slug_id>/', show_post, name = 'post'),
    path('login', login, name = 'login'),
    path('category/<slug:slug_id>/', show_category, name = 'category'),
    ]