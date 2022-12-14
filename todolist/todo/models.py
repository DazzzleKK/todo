from django.db import models
from django.conf import settings


class Tasks(models.Model):

    PRIORITIES = (
        ('1', 'Critical Priority'),
        ('2', 'High Priority'),
        ('3', 'Medium Priority'),
        ('4', 'Low Priority'),
    )

    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    completed = models.BooleanField(null=True, default=False)
    priority = models.CharField(max_length=50, choices=PRIORITIES, default='1')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return f'{self.title} --- {self.content}'
