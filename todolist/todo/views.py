from django.views.generic import ListView, CreateView, DeleteView, UpdateView, View
from django.urls import reverse_lazy
from .forms import NewTaskForm, EditTaskForm
from .models import Tasks
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.


# def register(request):
#     form = UserCreationForm()
#     return render(request, 'todo/register.html', {'form': form})

class SignUpView(CreateView):
    template_name = 'todo/auth/register.html'
    success_url = reverse_lazy('login')
    form_class = UserCreationForm


class MyLoginView(LoginView):
    template_name = 'todo/auth/login.html'
    success_url = reverse_lazy('todolist')


class MyLogoutView(LogoutView):
    template_name = 'todo/auth/login.html'
    # next_page = 'login'
    


# class LoginView(View):
#     template_name = 'todo/login.html'
#     form_class = AuthenticationForm

#     def get(self, request):
#         form = self.form_class()
#         message = ''
#         return render(request, self.template_name, context={'form': form, 'message': message})

#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password'],
#             )
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#         message = 'Login failed!'
#         return render(request, self.template_name, context={'form': form, 'message': message})


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
