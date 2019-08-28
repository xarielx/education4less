from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author': 'Ariel Barboza',
        'title': 'Scholarship 1',
        'content': 'First scholarship',
        'date_posted': 'August 28th 2019'
    },
    {
        'author': 'Feo',
        'title': 'Scholarship 2',
        'content': 'Second scholarship',
        'date_posted': 'August 28th 2019'
    },

]


def home(request):
    context = {
        'posts': posts,
    }
    return render(request, 'scholarships/home.html', context)


def about(request):
    return render(request, 'scholarships/about.html', {'title': 'About'})
