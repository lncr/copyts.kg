from django.shortcuts import render, get_object_or_404
from .models import *

def main_page(request):
    show_list = Show.objects.all()
    return render(request, 'doit/main_page.html', context={'show_list':show_list})

def detail_page(request, slug):
    show = get_object_or_404(Show, slug__iexact=slug)
    return render(request, 'doit/detail_page.html', context={'show':show})

def episode_detail(request, slug):
    episode = get_object_or_404(Episode, slug__iexact=slug)
    return render(request, 'doit/episode_detail.html', context={'episode':episode})

def genre_related_shows(request, slug):
    genre=Genre.objects.get(slug__iexact=slug)
    show_list = genre.shows.all()
    return render(request, 'doit/main_page.html', context={'show_list':show_list})
