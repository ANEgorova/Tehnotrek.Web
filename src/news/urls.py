from django.conf.urls import url
from django.contrib import admin
from .views import NewsView
from .views import show_text

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', NewsView.as_view()),
    url(r'$', show_text),
    url(r'^(?P<news_id>\d+)/like/$', show_text),
]
