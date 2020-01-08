from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name='main_page_url'),
    path('<str:slug>/', detail_page, name='show_detail_url'),
    path('watch/<str:slug>/',episode_detail, name='episode_detail_url'),
    path('genre/<str:slug>/', genre_related_shows, name='genre_related_shows_url'),
]
