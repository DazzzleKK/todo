from django.urls import path
from .views import *
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', ToDoList.as_view(), name='todolist'),
    path('completed/', ToDoListCompleted.as_view(), name='completed'),
    path('add-task/', TaskCreateView.as_view(), name='createtask'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='delete'),
    path('edit/<int:pk>/', TaskEditView.as_view(), name='edit'),
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', MyLoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    # path('logout/', RedirectView.as_view(pattern_name='login'), name='logout'),
]
