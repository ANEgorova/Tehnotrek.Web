from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Task
from django import forms


class CreateTask(forms.Form):
    title = forms.CharField(label='Task Title')
    #  tags = forms ?? What field?
    text = forms.CharField(widget=forms.Textarea, label='Task Description')
    status = forms.ChoiceField(choices=(('DN', 'Do now'), ('WD', 'Will do')))

    def clean_data(self):
        text = self.cleaned_data['text']
        title = self.cleaned_data['title']
        #  Errors


def CreateTaskView(request):
    if request.method == 'POST':
        form = CreateTask(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            current_task = Task(
                author=request.user,
                title=data['title'],
                text=data['text'],
                status=data['status']
            )
            current_task.save()
            return redirect('/tasks/')
    else:
        form = CreateTask()
    return render(request, 'task/new_task.html', {'form': form})


class OnePostView(DetailView):
    model = Task
    slug_field = 'id'
    template_name = 'post.html'


class AllPostsView(ListView):
    template_name = 'task/post_list.html'
    model = Task

    # Create context, we don't need to draw everything in HTML
    def get_context_data(self, **kwargs):
        context = super(AllPostsView, self).get_context_data(**kwargs)
        form = CreateTask()
        context['form'] = form
        return context

