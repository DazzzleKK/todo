from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import NewTaskForm, EditTaskForm
from .models import Tasks

# Create your views here.


class ToDoList(ListView):
    model = Tasks
    template_name = 'todo/tasks_list.html'
    context_object_name = 'tasks'
    ordering = ['priority']
    # paginate_by = 10

    def get_queryset(self):
        return Tasks.objects.filter(completed=False).order_by('priority')


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
    # paginate_by = 10

    def get_queryset(self):
        return Tasks.objects.filter(completed=True).order_by('priority')


class TaskCreateView(CreateView):
    form_class = NewTaskForm
    template_name = "todo/new_task.html"
    success_url = reverse_lazy('todolist')


class TaskDeleteView(DeleteView):
    model = Tasks
    success_url = reverse_lazy('todolist')
