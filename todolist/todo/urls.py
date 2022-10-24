from django.urls import path
from .views import *

urlpatterns = [
    path('', ToDoList.as_view(), name='todolist'),
    path('completed/', ToDoListCompleted.as_view(), name='completed'),
    path('add-task/', TaskCreateView.as_view(), name='createtask'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='delete'),
    path('edit/<int:pk>/', TaskEditView.as_view(), name='edit'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
]
