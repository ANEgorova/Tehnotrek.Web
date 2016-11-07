from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import *


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', login_required(OnePostView.as_view()), name='one-post-detail'),
    url(r'newtask/$', login_required(CreateTaskView), name='new-task'),
    url(r'$', login_required(AllPostsView.as_view()), name='all-posts-detail'),
]
