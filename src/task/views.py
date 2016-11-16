from django.shortcuts import render, redirect, reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from .models import Task
from django import forms


#  Form for creating new task
class CreateTask(forms.Form):
    title = forms.CharField(label='Task Title')
    #  tags = forms ?? What field?
    text = forms.CharField(widget=forms.Textarea, label='Task Description')
    status = forms.ChoiceField(choices=(('DN', 'Do now'), ('WD', 'Will do')))


#  Function to create new task
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


# class OnePostView(DetailView):
#     model = Task
#     slug_field = 'id'
#     template_name = 'post.html'


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
    template_name = 'task/task.html'
    fields = (
        'title',
        'text',
        'status'
    )

    def get_success_url(self):
        return reverse('tasks:all-posts-detail')


class UserTasksView(ListView):
    template_name = 'task/user_task.html'
    model = Task

    def get_queryset(self):
        qs = super(UserTasksView, self).get_queryset()

        qs = qs.filter(author=self.request.user).order_by('pub_data')
        return qs


