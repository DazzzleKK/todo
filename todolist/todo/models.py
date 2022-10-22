from re import T
from django.db import models

# Create your models here.




class Tasks(models.Model):

    PRIORITIES = (
        ('CRITICAL', 'Critical Priority'),
        ('HIGH', 'High Priority'),
        ('MEDIUM', 'Medium Priority'),
        ('LOW', 'Low Priority'),
        ('TRIVIAL', 'High Priority'),
    )

    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    completed = models.BooleanField(null=True)
    priority = models.CharField(max_length=50, choices=PRIORITIES)

    def __str__(self):
        return f'{self.title} --- {self.content}'