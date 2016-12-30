from django.conf.urls import url
from django.contrib.auth.views import login, logout
from django.urls import reverse_lazy
from views import register_user

urlpatterns = [
    url(r'^login/$', login, name='login', kwargs={'template_name': 'login.html'}),
    url(r'^logout/', logout, name='logout', kwargs={'template_name': 'logout.html', 'next_page': reverse_lazy('accounts:login')}),
    url(r'join/', register_user, name='registration'),
]
