from django.urls import path
from .views import *

urlpatterns = [
    path('', womens, name = 'womens'),
    path('about/', about, name = 'about'),
    path('add_post/', add_post, name = 'add_post'),
    path('contacts/', contacts, name = 'contacts'),
    path('post/<slug:slug_id>/', show_post, name = 'post'),
    path('login', login, name = 'login'),
    path('category/<slug:slug_id>/', show_category, name = 'category'),
    ]