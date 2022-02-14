from django.shortcuts import render
from django.views.generic import ListView
from news.models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
