from django.conf.urls import url
from django.contrib.auth.views import login

from .views import *

urlpatterns = [
    url(r'', login, name='login', kwargs={'template_name': 'main.html'})
]
