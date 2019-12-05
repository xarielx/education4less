# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import Scholar
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .filters import ScholarFilter
from . import filters
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    scholar_list = Scholar.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(scholar_list, 5)
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


def search(request):
    return render(request, 'scholar/user_search.html', {'title': 'About'})


def search(request):
    # paginate_by = 10
    # user_list = Scholar.objects.all()
    # user_filter = ScholarFilter(request.GET, queryset=user_list)
    # return render(request, 'scholar/user_search.html', {'filter': user_filter})
    paginate_by = 5
    filtered_qs = Scholar.objects.all()
    user_filter = ScholarFilter(request.GET, queryset=filtered_qs)
    paginator = Paginator(user_filter.qs, 5)

    page = request.GET.get('page')
    try:
        scholars = paginator.page(page)
    except PageNotAnInteger:
        scholars = paginator.page(1)
    except EmptyPage:
        scholars = paginator.page(paginator.num_pages)

    return render(
        request,
        'scholar/user_search.html',
        {'filter': user_filter, 'scholars': scholars})
