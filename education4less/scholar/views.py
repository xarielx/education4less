# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Scholar
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    scholar_list = Scholar.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(scholar_list, 10)
    try:
        scholars = paginator.page(page)
    except PageNotAnInteger:
        scholars = paginator.page(1)
    except EmptyPage:
        scholars = paginator.page(paginator.num_pages)
    context = {
        'posts': Scholar.objects.all(),
    }
    return render(request, 'scholar/home.html', {'scholars': scholars})


def about(request):
    return render(request, 'scholar/about.html', {'title': 'About'})
