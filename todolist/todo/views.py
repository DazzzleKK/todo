from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from .forms import NewTaskForm
from .models import Tasks

# Create your views here.


class ToDoList(ListView):
    model = Tasks
    template_name = 'todo/tasks_list.html'
    context_object_name = 'tasks'
    ordering = ['priority']
    # paginate_by = 10


class TaskCreateView(CreateView):
    form_class = NewTaskForm
    template_name = "todo/new_task.html"
    success_url = reverse_lazy('todolist')


class TaskDelete(DeleteView):
    model = Tasks
    success_url = reverse_lazy('todolist')
