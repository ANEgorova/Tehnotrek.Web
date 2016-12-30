from django.shortcuts import render, redirect, reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from .models import Task
from django import forms

import logging
logger = logging.getLogger('task.view')


#  Form for creating new task
class CreateTask(forms.Form):
    title = forms.CharField(label='Task Title')
    #  tags = forms ?? What field?
    text = forms.CharField(widget=forms.Textarea, label='Task Description')
    status = forms.ChoiceField(choices=(('DN', 'Do now'), ('WD', 'Will do')))


#  Function to create new task
def create_task_view(request):
    logger.debug("Debug!")
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


#  View to see all tasks of all users
class AllPostsView(ListView):
    template_name = 'task/tasks_list.html'
    model = Task

    # Create context, we don't need to draw everything in HTML
    def get_context_data(self, **kwargs):
        context = super(AllPostsView, self).get_context_data(**kwargs)
        form = CreateTask()
        context['form'] = form
        return context


#  View for editing one task for one user
class TaskView(UpdateView):
    model = Task
    slug_field = 'id'
    template_name = 'task/edit_task.html'
    fields = (
        'title',
        'text',
        'status'
    )

    def get_success_url(self):
        return reverse('tasks:all-posts-detail')


#  View for observing tasks from one person
class UserTasksView(ListView):
    template_name = 'task/user_tasks.html'
    model = Task

    def get_queryset(self):
        qs = super(UserTasksView, self).get_queryset()

        qs = qs.filter(author=self.request.user).order_by('pub_data')
        return qs


class FilterForm(forms.Form):
    tasks = forms.ModelChoiceField(Task.objects.all())
    #  filter_key = forms.ModelChoiceField(choices=(('AN', 'Author name'),
    #  ('D', 'Date'), ('TT', 'Task Title'), ('S', 'Status')))


def view_filter(request):

    def sort_by_date(self):
        tasks_by_name = Task.objects.order_by('pub_data')

    filter_form = FilterForm()
    return render(request, 'task/filter_task.html', {'form': filter_form})
