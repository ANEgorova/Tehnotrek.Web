from django.shortcuts import render, HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Post


class OnePostView(DetailView):
    model = Post
    slug_field = 'id'
    template_name = 'post.html'


class AllPostsView(ListView):
    template_name = 'task/post_list.html'
    model = Post


