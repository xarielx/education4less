from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='scholar-home'),
    path('about/', views.about, name='scholar-about'),
    path('search/', views.search, name='scholar-search'),
]
