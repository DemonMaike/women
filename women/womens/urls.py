from atexit import register
from django.urls import path
from .views import *

urlpatterns = [
    path('', WomenHome.as_view(), name = 'womens'),
    path('about/', about, name = 'about'),
    path('add_post/', AddPost.as_view(), name = 'add_post'),
    path('contacts/', contacts, name = 'contacts'),
    path('post/<slug:slug_id>/', Show_post.as_view(), name = 'post'),
    path('login/', LoginUser.as_view(), name = 'login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('category/<slug:slug_id>/', WomenCategory.as_view(), name = 'category'),
    path('logout/', logout_user, name = 'logout'),
    ]