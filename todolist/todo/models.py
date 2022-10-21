from re import T
from django.db import models

# Create your models here.

class Tasks(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    completed = models.BooleanField(null=True)

    def __str__(self):
        return f'{self.title} --- {self.content}'