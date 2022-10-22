from django import forms
from .models import Tasks


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