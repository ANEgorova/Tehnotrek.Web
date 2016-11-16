from django.conf.urls import url
from django.contrib.auth.views import login, logout
from views import register_user

urlpatterns = [
    url(r'^login/$', login, name='login', kwargs={'template_name': 'login.html'}),
    url(r'^logout/', logout, name='logout', kwargs={'template_name': 'logout.html'}),
    url(r'join/', register_user, name='registration'),
]
