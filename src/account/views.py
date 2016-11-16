from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import User


class MyRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('name', 'username', 'email', 'avatar', 'password1')

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.name = self.cleaned_data['name']
        user.username = self.cleaned_data['username']
        user.avatar = self.cleaned_data['avatar']
        user.password = self.cleaned_data['password1']
        user.set_password(user.password)

        if commit:
            user.save()
        return user


def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # new_user = authenticate(username=form.cleaned_data['username'],
            #                         password=form.cleaned_data['password1'],
            #                        )
            # login(request, new_user)
            return HttpResponseRedirect('/')
    else:
        form = MyRegistrationForm()
    return render(request, 'join.html', {'form': form})
