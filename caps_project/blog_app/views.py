from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post


# Class Based Views
class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = ('title', 'author', 'body')


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ('title', 'body')
