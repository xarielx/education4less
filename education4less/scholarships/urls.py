from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='scholarships-home'),
    path('about/', views.about, name='scholarships-about'),
]
