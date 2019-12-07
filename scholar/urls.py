from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

urlpatterns = [
    path('', views.home, name='scholar-home'),
    path('about/', views.about, name='scholar-about'),
    path('search/', views.search, name='scholar-search'),

]
