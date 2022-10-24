from django import forms
from .models import Tasks
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation


class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'content', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control bg-secondary', 'placeholder': 'New Task'}),
            'priority': forms.Select(attrs={'class': 'form-control bg-secondary'}),
            'content': forms.Textarea(attrs={'class': 'form-control bg-secondary', 'rows': 3}),
        }


class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'content', 'priority', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control bg-secondary'}),
            'priority': forms.Select(attrs={'class': 'form-control bg-secondary'}),
            'content': forms.Textarea(attrs={'class': 'form-control bg-secondary', 'rows': 5}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input bg-primary'}),
        }


class MyUserCreationForm(UserCreationForm):
    username = forms.CharField(required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password1 = forms.CharField(label=('Password'),
                                widget=(forms.PasswordInput(attrs={'class': 'form-control'})),
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label=('Password Confirmation'), widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                help_text=('Just Enter the same password, for confirmation'))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

