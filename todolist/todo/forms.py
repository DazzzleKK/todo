from django import forms
from .models import Tasks


class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'content', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control-sm bg-secondary'}),
            'priority': forms.Select(attrs={'class': 'form-control-sm bg-secondary'}),
            'content': forms.Textarea(attrs={'class': 'form-control bg-secondary', 'rows': 5}),
        }