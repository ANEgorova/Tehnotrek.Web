from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView
from .models import Article


class NewsView(DetailView):

    model = Article
    template_name = 'article.html'


def show_text(request, news_id=0, cat_id=0):
    return HttpResponseRedirect('http://yandex.ru/')
