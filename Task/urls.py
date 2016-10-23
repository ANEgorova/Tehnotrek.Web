from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', OnePostView.as_view(), name='one-post-detail'),
    url(r'$', AllPostsView.as_view(), name='all-posts-detail'),
]

