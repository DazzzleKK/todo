from django.views.generic import ListView, CreateView, DeleteView, UpdateView, View
from django.urls import reverse_lazy
from .forms import NewTaskForm, EditTaskForm, MyUserCreationForm
from .models import Tasks
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings


# Create your views here.


# def register(request):
#     form = UserCreationForm()
#     return render(request, 'todo/register.html', {'form': form})

class SignUpView(CreateView):
    template_name = 'todo/auth/register.html'
    success_url = reverse_lazy('login')
    form_class = MyUserCreationForm


class MyLoginView(LoginView):
    template_name = 'todo/auth/login.html'
    success_url = reverse_lazy('todolist')


class MyLogoutView(LogoutView):
    template_name = 'todo/auth/login.html'


class ToDoList(ListView):
    model = Tasks
    template_name = 'todo/tasks_list.html'
    context_object_name = 'tasks'
    ordering = ['priority']
    # paginate_by = 10

    def get_queryset(self):
        if self.request.user.username:
            return Tasks.objects.filter(author=self.request.user).filter(completed=False).order_by('priority')
        else:
            return None


class TaskEditView(UpdateView):
    model = Tasks
    form_class = EditTaskForm
    template_name = "todo/edit_task.html"
    success_url = reverse_lazy('todolist')


class ToDoListCompleted(ListView):
    model = Tasks
    template_name = 'todo/completed_tasks_list.html'
    context_object_name = 'tasks'
    ordering = ['priority']

    def get_queryset(self):
        if self.request.user.username:
            return Tasks.objects.filter(author=self.request.user).filter(completed=True).order_by('priority')
        else:
            return None


class TaskCreateView(CreateView):
    form_class = NewTaskForm
    template_name = "todo/new_task.html"
    success_url = reverse_lazy('todolist')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskDeleteView(DeleteView):
    model = Tasks
    success_url = reverse_lazy('todolist')
