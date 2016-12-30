from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.views import login
from django.contrib.auth import login as auth_login
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from .models import User


class MyRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('name', 'username', 'email', 'avatar', 'password1')

        labels = {
            'name': 'Full name',
            'username': 'Username',
            'password1': 'Password',
        }

        help_texts = {}

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.name = self.cleaned_data['name']
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.avatar = self.cleaned_data['avatar']
        user.password = self.cleaned_data['password1']
        user.set_password(user.password)

        if commit:
            user.save()
        return user


def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save()
            #  user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            auth_login(request, user)
            return HttpResponseRedirect("/tasks/")
    else:
        form = MyRegistrationForm()
    return render(request, 'join.html', {'form': form})

